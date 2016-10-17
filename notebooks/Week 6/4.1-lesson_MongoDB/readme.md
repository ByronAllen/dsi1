Week 6| Lesson 4.1

### **LEARNING OBJECTIVES**

*After this lesson, you will be able to:* - Explain what a NoSQL database is and how it is from a relational database. Carry out the normal tasks using MongoDB.

### **STUDENT PRE-WORK**

*Before this lesson, you should already have an idea:* - About relational databases and the operations of a database.

### **LESSON GUIDE**

| TIMING | TYPE                                                                | TOPIC                                      |
|--------|---------------------------------------------------------------------|--------------------------------------------|
| 15 min | [Introduction](#introduction)                                       | Intro to MongoDB                           |
| 10 min | [Installation](#mongodb-installation)                               | Installing MongoDB                         |
| 20 min | [Guided Practice](#guided-practice)                                 | Guided Practice: Introduction to pymongo   |
| 15 min | [Ind-practice](http://api.mongodb.com/python/current/tutorial.html) | Independent Practice: functions of pymongo |
| 5 min  | [Conclusion](#conclusion)                                           | Conclusion                                 |

**Introduction**
================

MongoDB is a cross-platform, document oriented database that provides, high performance, high availability, and easy scalability. It is one of the NoSQL databases. MongoDB works on concept of collection and document.

**In MongoDB…**
---------------

-   ***Database:*** a physical container for collections. Each database has its own set of files on the file system. A single MongoDB server typically has multiple databases.

-   ***Collection:*** a group of MongoDB documents equivalent of an RDBMS table. A collection exists within a single database. Collections do not enforce a schema. Documents within a collection can have different fields. Typically, all documents in a collection are of similar or related purpose.

-   ***Document:*** a set of key-value pairs. Documents have dynamic schema. Dynamic schema means that documents in the same collection do not need to have the same set of fields or structure, and common fields in a collection's documents may hold different types of data. Similar to JSON objects

**MongoDB vs RDBMS**
--------------------

| **RDBMS**                        | **MongoDB**                                               |
|----------------------------------|-----------------------------------------------------------|
| Database                         | Database                                                  |
| Table                            | Collection                                                |
| Tuple/Row                        | Document                                                  |
| Column                           | Field                                                     |
| Table Join                       | Embedded Documents                                        |
| Primary Key                      | Primary Key (Default key \_id provided by mongodb itself) |
| ***Database Server and Client*** |
| Mysqld/Oracle                    | mongod                                                    |
| mysql/sqlplus                    | mongo                                                     |

Sample Document

{

    \_id: ObjectId(7df78ad8902c)

    title: 'MongoDB Overview',

    description: 'MongoDB is no sql database',

    by: 'tutorials point',

    url: 'http://www.tutorialspoint.com',

    tags: \['mongodb', 'database', 'NoSQL'\],

    likes: 100,

    comments: \[

        {

            user:'user1',

            message: 'My first comment',

            dateCreated: new Date(2011,1,20,2,15),

            like: 0

        },

        {

            user:'user2',

            message: 'My second comments',

            dateCreated: new Date(2011,1,25,7,45),

            like: 5

        }

    \]

}

**\_id** is a 12 bytes hexadecimal number which assures the uniqueness of every document. You can provide \_id while inserting the document. If you don’t provide then MongoDB provides a unique id for every document. These 12 bytes first 4 bytes for the current timestamp, next 3 bytes for machine id, next 2 bytes for process id of MongoDB server and remaining 3 bytes are simple incremental VALUE.

**Advantages of MongoDB over RDBMS**
------------------------------------

-   **Schema less** − MongoDB is a document database in which one collection holds different documents. Number of fields, content and size of the document can differ from one document to another.

-   Structure of a single object is clear.

-   No complex joins.

-   Deep query-ability. MongoDB supports dynamic queries on documents using a document-based query language that's nearly as powerful as SQL.

-   **Ease of scale-out** − MongoDB is easy to scale.

-   Conversion/mapping of application objects to database objects not needed.

-   Uses internal memory for storing the (windowed) working set, enabling faster access of data.

**Why Use MongoDB?**
--------------------

-   **Document Oriented Storage** − Data is stored in the form of JSON style documents.

-   Index on any attribute

-   Replication and high availability

-   Rich queries

-   Fast in-place updates

-   Professional support by MongoDB

**Where to Use MongoDB?**
-------------------------

-   Big Data

-   Content Management and Delivery

-   Mobile and Social Infrastructure

-   User Data Management

-   Data Hub

**MongoDB Installation:**
-------------------------

-   To use it on python: “pip install pymongo”

-   On windows: <https://pypi.python.org/pypi/pymongo/>

*Installing MongoDB *

-   You can download MongoDB from here: [https://www.mongodb.com/download-center?jmp=nav\#community](https://www.mongodb.com/download-center?jmp=nav%23community)

-   Installation guide: <https://docs.mongodb.com/manual/administration/install-community/>

    -   Linux: <https://docs.mongodb.com/manual/administration/install-on-linux/>

        -   Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>

        -   Ubuntu 15.04/15.10: <https://rohan-paul.github.io/mongodb_in_ubuntu/2015/09/03/How_to_Install_MongoDB_Iin_Ubuntu-15.04.html>

        -   Adding a source line in Ubuntu <https://help.ubuntu.com/community/Repositories/CommandLine>

> <http://askubuntu.com/questions/197564/how-do-i-add-a-line-to-my-etc-apt-sources-list>

-   Windows: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/>

-   OS X: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/>

**Guided Practice**
-------------------

https://github.com/ga-students/DSI-SYD-1/blob/master/classes/week-06/4.1-lesson/code/MongoDB_test.ipynb

**Conclusion**
--------------

MongoDB is a NoSQL database with high performance. It uses a rich query language and support for multiple storage engines.

**Additional Material**
-----------------------

1.  [Introduction to MongoDB](https://docs.mongodb.com/manual/introduction/)

2.  [Getting started with MongoDB (Python Edition)](https://docs.mongodb.com/getting-started/python/)

3.  [PyMongo Documentation](http://api.mongodb.com/python/current/tutorial.html)

4.  [MongoDB in 30 Minutes](https://www.youtube.com/watch?v=pWbMrx5rVBE/)

**References**
--------------

1.  <https://www.tutorialspoint.com/mongodb/index.htm>

2.  <https://docs.mongodb.com/getting-started/python/>
