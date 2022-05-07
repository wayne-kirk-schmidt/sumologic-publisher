Business Background
===================

When you are building your applications, sometimes your machine data won't be in the form of log files. What then?

For modern Continuous Integration and Deployment, we sometimes need to have documentation ingested, outside the bounds of JSON or CSV.

Business Challenge
==================

We need to be able to have our Sumo Logic environment be able to accept output from our CI/CD pipeline and easily process that input.

Since our pipelines will be based on commands and webhooks our solution needs to embrace being run when a job is completed, started when the job is finished by the platform providing the build.

Also, we need to be able to understand any type of content, not just CSV or JSON, so this extends to PDF files, Microsoft and Google document formats as well; in short, we need to embrace being able to ingest anything and be able to match that file with relevant text within.

Business Cases
==============

Here are a sample of questions you want to have answers for to help your teams. Each of these questions deals with change.

* What documents support the changes we see in our log files?

* Can we build a map of those documents and track changes to those files?

* Can we work with the CI/CD pipeline to ingest the files and extract out the text we need?

Business Solution
=================

Our solution using "Sumo on Sumo", feeding Sumo Logic data about how people are working with Sumo Logic to help your business.

And, best of all, this can be done in several easy steps:

- Create a HTTPS collector using these [steps](https://help.sumologic.com/03Send-Data/Hosted-Collectors).

- Create a HTTPS source using these [steps](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors).

- Set up the ingest script following the [readme](../README.md).

- Run the script! Now you can check the source categories for the data you want to see.

Business Benefits
=================

We can identify the file types of most of your development environment, and ingest them using the hosted collector.

The result? We can use this tool to help build a map, of the file path, the checksum of the file, and the extracted text.

Couple this with the permissions, ownership, and the date, and we can easily plot the changes within your environment.

Examples
========

![example1](publisher1.png)

![example2](publisher2.png)

