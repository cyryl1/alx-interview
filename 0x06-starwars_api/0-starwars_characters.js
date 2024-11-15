#!/usr/bin/node
/**
 * Wrapper function for request object that allows it
 * to work with async and await
 * @param {String} url - site url
 * @returns {Promise}  - promise object
 */
function makeRequest (url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

/**
 * Entry point - send a request to starwars api
 * to retrieve info on each movie character then print the names
 */
async function main () {
  const args = process.argv;

  if (args.length < 3) return;
  const movieId = args[2];

  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  const movie = await makeRequest(url);

  if (movie.characters === undefined) return;
  for (const characterUrl of movie.characters) {
    const character = await makeRequest(characterUrl);
    console.log(character.name);
  }
}

main();

// const request = require('request');

// // Get the movie ID from command line arguments
// const movieId = process.argv[2];

// if (!movieId) {
//   console.error('Usage: ./0-starwars_characters.js <movie_id>');
//   process.exit(1);
// }

// const url = `https://swapi.dev/api/films/${movieId}/`;

// request(url, { json: true }, (error, response, body) => {
//   if (error) {
//     console.error('Error fetching movie:', error);
//     process.exit(1);
//   }

//   if (response.statusCode !== 200) {
//     console.error(`Failed to retrieve movie. Status Code: ${response.statusCode}`);
//     process.exit(1);
//   }

//   const characters = body.characters;

//   if (!characters) {
//     console.error('No characters found for this movie.');
//     return;
//   }

//   characters.forEach((characterUrl) => {
//     request(characterUrl, { json: true }, (error, response, characterBody) => {
//       if (error) {
//         console.error('Error fetching character:', error);
//         return;
//       }
//       if (response.statusCode === 200) {
//         console.log(characterBody.name);
//       } else {
//         console.error(`Failed to retrieve character. Status Code: ${response.statusCode}`);
//       }
//       // Exit the script after fetching all characters
//       process.exit(0);
//     });
//   });
// });
