# Teacher-Statistics
Applied analytical datasets of teacher's performance from the student records. Contains all the teachers who were in 3rd semester of **Computer Science**[II Year & III Year], **Aerospace**[II Year], **Automobile**[II Year], **Civil**[II Year], **Electronics and Communication**[II Year], **Electronics and Electrical**[II Year], **Mechanical**[II Year] and **Mechatronics[II Year]**.

![image] (https://raw.githubusercontent.com/poke19962008/Teacher-Stats/master/git-res/s1.png?token=AI2atF556vbAs-SeaNRDaDZrxj374QOkks5WslaPwA%3D%3D)

## How to run

### Setting up MongoDB

Set up Mongo DataBase named **teacher**

```
$ cd parser
$ python mongoInserter.py
```

### Setting up node servers

This will start the servers on http://localhost:3800/. Access from **http://localhost:3800/teacher**.

```
$ node index.js
```

## LICENSE

Copyright © 2015 SAYAN DAS

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

