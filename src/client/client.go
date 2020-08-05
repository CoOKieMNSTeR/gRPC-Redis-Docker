package main

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"main/proto"
	"os"
	"time"

	"google.golang.org/grpc"
)

var (
	serverAddr = flag.String("server_addr", "localhost:4040", "The server address in the format of host:port")
)

type Users struct {
	ID        string `json:"id"`
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Email     string `json:"email"`
	Gender    string `json:"gender"`
	IPAddress string `json:"ip_address"`
	UserName  string `json:"user_name"`
	Agent     string `json:"agent"`
	Country   string `json:"country"`
}

func recordResult(client proto.GrpcServiceClient, SetPerson *proto.SetPerson) {
	log.Printf("Kaydedilen kişi id = %s, %s", SetPerson.Key, SetPerson.Value)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	person, err := client.RecordDB(ctx, SetPerson)
	if err != nil {
		log.Fatalf("%v.RecordDB(_) = _, %v: ", client, err)
	}
	log.Println(person)
}

func getRecordResult(client proto.GrpcServiceClient, GetPerson *proto.GetPerson) {
	log.Printf("Aranan kişi id = %s", GetPerson.Key)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	person, err := client.GetRecordDB(ctx, GetPerson)
	if err != nil {
		log.Fatalf("%v.RecordDB(_) = _, %v: ", client, err)
	}
	log.Println(person)
}

func readJSON() (string, error) {
	jsonFile, err := os.Open("C:/Go/challange/src/users/1.json")
	if err != nil {
		fmt.Println(err)
	}
	defer jsonFile.Close()

	dec := json.NewDecoder(jsonFile)

	_, err = dec.Token()
	if err != nil {
		log.Println(err)
	}

	var user Users
	for dec.More() {
		err = dec.Decode(&user)
		if err != nil {
			log.Println(err)
		}
		return user.FirstName, nil
	}

	_, err = dec.Token()
	if err != nil {
		log.Println(err)
	}

	return "", nil
}

func main() {
	flag.Parse()
	var opts []grpc.DialOption
	opts = append(opts, grpc.WithInsecure())
	opts = append(opts, grpc.WithBlock())
	conn, err := grpc.Dial(*serverAddr, opts...)
	if err != nil {
		log.Fatalf("fatal to dial: %v", err)
	}
	defer conn.Close()
	client := proto.NewGrpcServiceClient(conn)
	name, err := readJSON()
	fmt.Println(name)
	recordResult(client, &proto.SetPerson{Key: "1", Value: name})
	getRecordResult(client, &proto.GetPerson{Key: "1"})
}
