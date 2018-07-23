#!/bin/bash

if ! ./Date/Mangas.txt -f 
then
    echo >> ./Date/Mangas.txt
fi

if ! ./Date/Animes.txt -f 
then
    echo >> ./Date/Animes.txt
fi

if ! ./Date/Movies.txt -f 
then
    echo >> ./Date/Movies.txt
fi

if ! ./Date/Series.txt -f 
then
    echo >> ./Date/Series.txt
fi

if ! ./Date/Courses.txt -f 
then
    echo >> ./Date/Courses.txt
fi

if ! ./Date/Novels.txt -f 
then
    echo >> ./Date/Novels.txt
fi