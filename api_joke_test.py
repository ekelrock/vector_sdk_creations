#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""API Joke Test - Vector will tell you a random Chuck Norris joke"""

# Import the requests module we'll use to access and parse the JSON data
import requests
import anki_vector


# Here is the documentation for the API we'll be using: http://www.icndb.com/api/
# For this simple example, we'll request a single random joke with no additional parameters
response = requests.get('http://api.icndb.com/jokes/random')
data = response.json()

# The data response in this case is a JSON formatted dict. Here's an example of the response format:
# {
#    "type":"success",
#    "value":{
#       "id":565,
#       "joke":"Chuck Norris can make a class that is both abstract and final.",
#       "categories":[
#          "nerdy"
#       ]
#    }
# }


# Check if the API call was successful. If not, we cannot proceed.
if response.status_code != 200:
    print("The API call was unsuccessful. Please try again later.")
    exit()


# Ok, our API call must have been successful :)
# We'll use the key value pairs to access the data from the JSON dict and print the results
# Note that it is not necessary to print any of this information. This is only here for demonstration and learning purposes

# Since we're concatenating the keys and values, we'll need to convert any non-string to a string with the "str()" function
# The "type" is a simple string so we can print that without modification
print("Type: " + data["type"])

# The "id" is an integer so we need to convert it to a string to concatenate and print it
# Also notice the format we're using to access nested information: var[top_key][nested_key]
valueIdStr = str(data["value"]["id"])
print("Value ID: " + valueIdStr)

# The "joke" is another string so we can print that as well
print("Value Joke: " + data["value"]["joke"])

# The "categories" is a nested array so we'll need to handle the possiblites of 0, 1, or 2+ possible values for this key
# Note: In limited testing it appears that there's never more than 1 "category", but this handles the possiblity of more
# First we'll get the number of "categories" using the "len()" function
numberOfCategories = len(data["value"]["categories"])
# Next we'll print that out into something readable; note that we're converting the integer to a string again here
print("Number of Categories: " + str(numberOfCategories))
# Now we can print all of the "categories" from this response
# Check to see if there are any "categories" at all. If not, no need to print anything here
if (numberOfCategories > 0) :
    # If there are more than 0 "categories", we'll loop through them and print their values
    for x in range(0, numberOfCategories) :
        # Create a nice list of readable outputs for our reference by concatenating some text, the item position in the array, and the value
        # Note that the item postion in the array is "str(x+1)" - since the loop starts with 0, we add 1 and convert it to a string to concatenate it
        # Note the format we use to access the nested information: var[top_key][nested_key][array_position]
        print("Value Category " + str(x+1) + ": " + data["value"]["categories"][x])


# And finally, we'll tell Vector to read the joke out load with the "robot.say_text()" function
# Note that this is taken directly from the Hello World tutorial included with the SDK
def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        # Here is where we tell Vector to speak the value of the "joke" key from the API's response
        robot.say_text(data["value"]["joke"])


if __name__ == "__main__":
    main()
