.. include:: <s5defs.txt>

=================
Selenium Workshop
=================

:Authors: Baiju Muthukadan
:Organization: ZeOmega, Bangalore
:Time: 3 hours

.. container:: handout

   Before the workshop starts ensure everyone has the prerequisites ready.

.. contents::
   :class: handout

.. |bullet| unicode:: U+02022

.. footer:: PyCON India 2013, Bangalore |bullet| 30-August-2013

Prerequisites
=============

- Laptop
- Operating System: Windows 7 or GNU/Linux
- Softwares: Python 2.7, Firefox & Text Editor
- Internet connection

About me
========

.. class:: small

- Python developer working as a Technical Architect at ZeOmega, Bangalore.
- Contributor to Zope project since 2006
- Authored the book titled, A Comprehensive Guide to Zope Component Architecture
- Founded the Swathanthra Malayalam Computing project in 2001 while studying at REC, Calicut
- Employed by Free Software Foundation of India in 2002-2003
- Conducted many Python related talks and workshops in various parts of India including FOSS.IN
- Contributed to Selenium Python documentation

Introduction to Selenium Webdriver
==================================

- History
- Example of where it is used
- Multiple language
- Multiple browser (Chrome, Opera, Firefox, IE, Safari)

.. container:: handout

   - The story starts in 2004 at ThoughtWorks in Chicago, with Jason Huggins
   - Shinya Kasatani started IDE
   - Simon Stewart started Webdriver

Outline of the Session
======================

- A sample web application written using bottle web framework will be used as the application under test (AUT)
- All the code will be available in a git repo: https://github.com/baijum/selenium_workshop
- Installation and setting up of the Selenium test environment
- Writing simple browser automation using Selenium webdriver API
- The stock application created will be used to write more test cases
- The test cases will be run using py.test testing tool


Setting up Selenium test environment (1)
========================================

https://github.com/baijum/selenium_workshop/archive/master.zip

Get the sample code::

  wget -c http://git.io/Tb7UJg -O selenium_workshop-master.zip

Extract & change to the project directory::

  unzip selenium_workshop-master.zip
  cd selenium_workshop-master

Setting up Selenium test environment (2)
========================================


Create a virtual environment::

  python virtualenv.py  ve

Activate virtual environment::

  source ve/bin/activate

Prepare for development (This step also install dependencies)::

  python setup.py develop

Initial database::

  python create_db.py

Running Application
===================

Activate virtual environment::

  source ve/bin/activate

Run todo application::

  python todo.py

You can access the application here: http://localhost:8080/

Running Test
============

Open another shell and activate virtual environment::

  source ve/bin/activate

Run test::

  py.test test_todo.py

Thanks
======

- Baiju Muthukadan
- Email: baiju.m.mail@gmail.com
