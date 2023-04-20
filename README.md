# Flight Tracker

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/Logo Whiteout.png">
  <source media="(prefers-color-scheme: light)" srcset="./images/Logo No BG.png">
  <img align="right" alt="Change image based on background theme." src="./images/Logo Whiteout.png">
</picture>

Flight Tracker is the best way for you to visualize flights. It was created by Ivan Ho, Alexander Houck, Anthony Johnson, Charlie Liu, Benjamin Rome, and Charles Tian as part of Rensselaer Polytechnic Institute's Software Design and Documentation course. Their goal is to create a basic and intuitive interface to visualize publicly available flight information.

Please visit [http://highflyers.pythonanywhere.com](http://highflyers.pythonanywhere.com/) to see a live deployment of Flight Tracker.

## Table of Contents
- [Background](#background)
- [Use Cases](#use-cases)
- [Local Deployment Setup Guide](#local-deployment-setup-guide)
- [Contributing](#contributing)
- [License](#license)

## Background
Flight planning is a difficult problem to solve for any shipping or passenger airline. It requires a lot of planning and reacting to opposing companies’ flight plans. Flight Tracker hopes to alleviate some of the pressure of this process by allowing users to filter flights by date, airline, time of day, and more, visualizing all flights that follow the user’s entered filters on a map. 

## Use Cases
Flight Tracker's interface allows the user to set various different filters to help them visualize and plan flights. Some of these filters include, but are not limited to, a starting and ending time, day of week, specific airlines, cargo and/or passenger airlines, starting destination, and ending destination.

## Requirements
- pandas ~= 1.3.2
- numpy ~= 1.21.1
- Flask ~= 2.0.1

## Local Deployment Setup Guide
Flight Tracker is built using all the requirements listed in the "requirements.txt" file. To install
you will need to follow the following steps:
1. Clone the repo into a local directory
2. Install NPM if you have not already
3. Run npm init in the chosen directory
4. Run npm install to install all the required packages
5. Install the Google Maps API with npm install @types/google__maps
6. In the directory run flask run
7. Open the link in your browser
8. Enjoy!

## Contributing
Contributions to Flight Tracker are greatly appreciated. Please note that we use the code styles imposed by [Black](https://black.readthedocs.io/en/stable/) for Python and [Prettier](https://prettier.io/docs/en/) for HTML, CSS, and JavaScript. We have auto-formatters and linters in place to ensure that all contributions adhere to these code styles.

## License
Flight Tracker is licensed under the MIT license, which can be viewed [here](LICENSE).
