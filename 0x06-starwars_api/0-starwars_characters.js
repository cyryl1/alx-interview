#!/usr/bin/node

const args = process.argv;
const movieId = args[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error: ', error);
  }

  if (response.statusCode === 200) {
    // console.log('Status Code: ', response.statusCode);
    const result = JSON.parse(body);
    const characters = result.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        if (error) {
          console.error('Error: ', error);
        }

        if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
