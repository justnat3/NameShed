<p align="center"><img width=12.5% src="https://user-images.githubusercontent.com/58314490/88469485-a45b3800-ceb7-11ea-86b7-b93700e85578.png"></p>

<h2 align="center">Machine Naming API </h2>


![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields)](http://makeapullrequest.com)

Tests:   
![.github/workflows/apiTest.yml](https://github.com/justnat3/MachineNameAPI/workflows/.github/workflows/apiTest.yml/badge.svg?branch=master)



# What is this?

Do you hate giving machines static names for generated environments? Me too. That is why I created this simple API.

The goal this API is to dynamically generate arbitrary machine names for your end-devices, servers, etc.

Use it and/or contribute to this repo as you please. Open to PR's


![image](https://user-images.githubusercontent.com/58314490/89093405-bdfcf380-d37f-11ea-953e-abd281f04141.png)


# How to Use 

What options do I have for endpoints?

- /prefixGen
  - This Endpoint requires a prefix=(String you wish to Prefix the result with), size=(Size of String generated)
  - Query example: /prefixGen?prefix=YourPrefix&size=5
  
  
- /nameGen
  - This Endpoint requires a size=(Size of string generated)
  - /nameGen?size=5
  
  
- /health 
  - This Endpoint lets you know the API health
- /
  - This Endpoint also lets you know the API health

Cheers,
Nate-
