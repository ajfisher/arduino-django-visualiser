Django Admin Visualiser
=======================

This is designed to get admin out of the django admin system in a quick and easy method such that it's possible to pass it across to arduino or other systems. It's not designed to be a hugely arcane or even remarkably secure system so please read the section on security precautions below.

Dependencies
------------

Dependencies for this to work are:

* Python 2.5+
    * Mechanize library
    * Beautiful Soup library
    * pyserial
* A working internet connection
* A Django site that you are an admin of 
* An arduino

Installation
------------

Everything is designed to run in situ if your dependencies are met.

As you're using Django it's unlikely you won't know how to do the following but just in case

pip install beautifulsoup mechanize pyserial

or

easy_install beautifulsoup mechanize pyserial 

Configuration
-------------

Take a copy of the python/conf.sample file as conf.py and then fill out the relevant details.

Of particular note is what screen you want mechanize to hit after login and also what paths to the HTML elements you need to get to.

Running
-------

From a terminal run python visualise.py and off you go.

To Do
-----

* write Arduino app to do this over serial (mostly done)
* write Arduino app to do this over network

