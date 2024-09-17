# Django-Storefront-App ( Python + Django )

# Prerequisites
## What you should know before taking this project
### Python
    - Basics 
    - Classes 
    - Inheritance
    - Polymorphism
### Relational Databases
    - Table 
    - Columns
    - Keys
    - Relationships 

## What is Django?

Django is free and open-source framework for building web apps with Python.

It helps us to build the website with lesstime with fewer line code.

## Companies using Django

- Youtube
- Instagram
- Spotify
- DropBox

Django is what we call batteries included with comes a lot of features so that we don’t have to code from the scratch.

## For example :-
## Django Features
- The admin site(interface)-managing our data which is huge time saver.
- Object-relational mapper(ORM) - that abstract database so we can query or precise data without  writing a lot of SQL code
- Authentication
- Caching data and much more

Saying the framework is better than Django -its kinda like saying Ferrari than truck coz it is faster. But if you wanna move something we are not going to use Ferrari for that. So Wise software engineer doesn’t pick up the framework merely base on performance. There is so many things we need to take in to count like maturity of framework, how stablility from one version to another, it’s learning curve, and size of cummunity and so on(Maturity, Stability, Difficulty, Community).

## How the Web Works
We learned that the <strong>django</strong> is the Django is a <strong>framework</strong> for building web applications with Python. Now let's talk about some of the fundamental concepts we need to understand to build web applications. Let's say we're going to build an online store and publish it at bridetool.com. 

Now, this website is going to have two parts or two applications a frontend and a backend. The frontend is the part that is liaded inside a web browser on a client machine, it's the part that the user sees and interacts with.

The backend is the part that runs on a web server, and is responsible for data processing, validating business rules, and so on. 

Now, let's imagine that Bikram wants to visit our website, so she points browser to bridetool.com. This address is also called a URL, which is short for Uniform Resource Locator is basically a way to locate a resources on our internet, a resource san be a webpage, and image, a video, a PDF, and so on, Bikram type bridetool.com and enter. At this moment,browser sends a request to the webserver that hosts our website and says, Hey, Bikram want to see the homepage. So the web server should takes this request, process it and return a response back to the client. This data exchange is defined by a protocal called HTTP, which is short for hypertext transfer protocol. It defines how clients and servers can communicate.

The big pictur is as Bikram navigates our website for each page, his browser sends an HTTP request to the server and receives an HTTP response. Now, as part of building the backend for this website, we need to decide how we're going to respond to clients. 

One option is to generate the requested page on the server and return it to the client. We use HTML for that. HTML is short for Hypertext Markup Language. It's a simple language for representing web pages and their content. Every web page we've seen on the internet is built using HTML. So one option is to generate the page on a server and return an HTML document to the client.

The other option is to return only the data needed on the requested page and have the client generate the page. So instead of putting a complete page or a complete HTML document  in an HTTP response, we only return the data like the list of products. 

Now what is the difference? Well, if we push this responsibility to the client, we can free up the server so it can serve more clients, our application will be more scalable. That's why over the past few years, this approach has become more trendy, and it's now considered the industry best practice. 

These days, we have tools like
- React
- Angular
- vue

For generating web pages on the client. These are all client side tools that are used by frontend developers. 

In contrash, we have server side tools for building backends. Django falls in this catagory. So we should not compare Django with let's say React. We may compare Django with other server side frameworks like
- Django
- ASP.NET core used by C# developer
- Express used by JavaScript developer and so on.

So if we push the responsibility of generating web pages to the client, the server essentially becomes a gateway to the data. On the  server, we can provide endpionts that the client can talk to, to get or save various pieces of data. For Example, we can provide one endpoint to get the list of products, and another endpoint to get the list of orders someone has placed. Now all these endpoints together represent the interface that clients use to talk to the server. In technical terms, We say the server provides an API, or an application programming interface to clients. The API is essentially like the buttons on a remote control. All these buttons together represent the interface or the API we use to interact with the TV. 

So, Our focus in the project is using Django to build an API for online store. Client applications can use his API to get or save the data. How these clients are build is irrelevant . Here we can use react, angular, or even plain JavaScript that falls under frontend development, which has nothing to do with Django. Once we build this API. If we know frontend development, we can always build a client app that talks to this API.

# Section-1: Django Fundamentals
- Introduction to Django
- Fundamentals of web development
- Setting up the development environment
- My first Django project
- 2 essential debugging techniques
