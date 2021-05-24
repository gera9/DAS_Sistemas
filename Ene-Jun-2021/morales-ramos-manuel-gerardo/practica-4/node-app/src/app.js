'use strict';

const xml2js = require('xml2js');
const fs = require('fs');
const parser = new xml2js.Parser({ attrkey: "ATTR" });
const mongoose = require('mongoose');

var people = [];

fs.readFile('src/people.xml', 'utf8', (error1, data) => {
    if(error1) return console.error(error1);
    
    parser.parseString(data, (error2, result) => {
        if(error2) return console.error(error2);

        result['people']['person'].forEach(element => {
  
            let person = {
                id: element['id'][0],
                first_name: element['first_name'][0],
                last_name: element['last_name'][0],
                company: element['company'][0],
                email: element['email'][0],
                ip_address: element['ip_address'][0],
                phone_number: element['phone_number'][0]
            };
            people.push(person);
        });
        

        //mongoose.connect('mongodb://localhost:27017/practica-4', {useNewUrlParser: true, useUnifiedTopology: true});
        mongoose.connect('mongodb://mongo_db:27017/practica-4', {
            useNewUrlParser: true, 
            useUnifiedTopology: true
        });
        const Person = mongoose.model('Person', {
            id: String,
            first_name: String,
            last_name: String,
            company: String,
            email: String,
            ip_address: String,
            phone_number: String
        });

        Person.insertMany(people).then(() => {
            console.log('Data insereted');

            process.exit();

        }).catch((error) => {
            console.error(error);

            process.exit();
        });

    });
});        