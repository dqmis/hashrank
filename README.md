# VU ISI Blockchain course's hashing function benchmark
Hashrank is a tool designed to help rank VU ISI hashing algorithms. This benchmark will determine how fast and reliable your algorithm works.

![](https://media.giphy.com/media/6Z3D5t31ZdoNW/giphy.gif)  

### The idea behind the benchmark
This benchmark is designed based on [Blockchain Group's practical task analysys](https://github.com/blockchain-group/Blockchain-technologijos/blob/master/pratybos/1uzduotis-Hashavimas.md) but with a few key changes:
1) The size of random strings is 1000 characters. This size was chosen because the most difficult part of hashing algorithm is the compression of the input and 5 character long string is too short to require any compression (most of the time only padding will be made).
2) Benchmark is not only calculating average of the similarity of pair of strings but also calculating the number of collisions it found.

### Requirements for the hashing algorithm
* It must accept string as `Console Argument`
* It returns hash as a simple console output.
* It must accept strings as long as 10000 characters
* It has to have CMake or Makefile to be able to easily build the executable

### What does this benchmark do?
It runs in three steps:
1) Gets reference time of basic letter collision test using SHA256 algorithm (credits to [emilisb](https://github.com/emilisb) for noticing this issue :D)
2) Calculates the average time of hashing every line of "Konstitucija.txt" file.
3) Calculates similarity score, time and collision number of pair of random strings that differ with one char
4) Calculates similarity score, time and collision number of pair of random strings

### How to run the benchmark
There are two main ways to do it:
1) The easy one: contact me at: `dom.seputis@gmail.com` and request me to run the benchmark for you in my machine (must submit the link to yours repository). Keep in mind that if there will be a lot of request I might not be able to run benchmark because of the shortage of time.
2) The longer, but more pleasant one (for me :D):  
* You need to setup `Python3` in your machine.
* Need to install progress bar module by running `$ pip / pip3 install tqdm`
* Build your executable by running `$ sh build.sh` and `clean.sh` to clean the directory.
* Run `$ python3 rank.py <name of the executable>`
* Add your results to the table below

To submit your results just make [PR](https://help.github.com/en/articles/creating-a-pull-request) with your entry in the table below:

**Legend**  
`A` - Average hashing time of "Konstitucija.txt"  
`B` - Letter collision test time  
`C` - Letter collision similarity average  
`D` - Number of collisions found in Letter test  
`E` - Word collision test time  
`F` - Word collision similarity average  
`G` - Number of collisions found in Word test  

| Github nick | Link to the repo            | Course/group | Reference test | A      | B          | C      | D    | E          | F      | G  |
|-------------|-----------------------------|--------------|----------------|--------|------------|--------|------|------------|--------|----|
| dqmis       | dqmis/vuhash                | 2/1          | 5.7301         | 0.0052 | 1417.6514  | 0.1108 | 9917 | 1497.0956s | 0.0056 | 0  |
| gytautele   | gytautele/blockchain        | 2/2          | 5.7201         | 0.0047 | 1043.5663  | 0.0136 | 0    | 1060.4037  | 0.0141 | 49 |
| emilisb     | emilisb/Hash                | 2/2          | 5.3863         | 0.0035 | 804.7102   | 0.0108 | 0    | 820.5668   | 0.0108 | 0  |
| gitguuddd   | gitguuddd/Hash_generatorius | 2/2          | 7.119          | 0.0285 | 6833.3648  | 0.0308 | 2    | 6840.2643  | 0.005  | 0  |
| zygisau     | zygisau/                    | 2/1          | 5.4321         | 0.0291 | 27320.3243 | 0.0148 | 96   | 27213.3451 | 0.0121 | 5  |
