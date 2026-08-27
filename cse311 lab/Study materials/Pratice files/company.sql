-- 1. Create Tables

CREATE TABLE department (
  dname VARCHAR(20) NOT NULL, -- Changed CHAR to VARCHAR for better memory management
  dnumber INT NOT NULL, -- Changed NUMERIC(1) to INT
  mgrssn CHAR(9) NOT NULL, -- Changed NUMERIC(9) to CHAR(9) to match SSN data type best practice
  mgrstartdate DATE NOT NULL,
  PRIMARY KEY (dnumber),
  UNIQUE (dname)
);

CREATE TABLE employee (
  fname VARCHAR(10) NOT NULL, -- Changed CHAR to VARCHAR
  lname VARCHAR(20) NOT NULL, -- Changed CHAR to VARCHAR
  ssn CHAR(9) NOT NULL, -- Changed NUMERIC(9) to CHAR(9)
  bdate DATE NOT NULL,
  address VARCHAR(30) NOT NULL, -- Changed CHAR to VARCHAR
  sex CHAR(1) NOT NULL,
  salary DECIMAL(7,2) NOT NULL, -- Changed NUMERIC(5) to DECIMAL(7,2) for standard currency storage
  superssn CHAR(9), -- Changed NUMERIC(9) to CHAR(9)
  dno INT NOT NULL, -- Changed NUMERIC(1) to INT
  PRIMARY KEY (ssn),
  FOREIGN KEY (dno) REFERENCES department(dnumber)
);

CREATE TABLE project (
  pname VARCHAR(20) NOT NULL, -- Changed CHAR to VARCHAR
  pnumber INT NOT NULL, -- Changed NUMERIC(2) to INT
  plocation VARCHAR(20) NOT NULL, -- Changed CHAR to VARCHAR
  dnum INT NOT NULL, -- Changed NUMERIC(1) to INT
  PRIMARY KEY (pnumber),
  UNIQUE (pname),
  FOREIGN KEY (dnum) REFERENCES department(dnumber)
);

CREATE TABLE works_on (
  essn CHAR(9) NOT NULL, -- Changed NUMERIC(9) to CHAR(9)
  pno INT NOT NULL, -- Changed NUMERIC(2) to INT
  hours DECIMAL(5,1), -- DECIMAL is better than NUMERIC for fixed-point math
  PRIMARY KEY (essn, pno),
  FOREIGN KEY (essn) REFERENCES employee(ssn),
  FOREIGN KEY (pno) REFERENCES project(pnumber)
);

CREATE TABLE dependent (
  essn CHAR(9) NOT NULL, -- Changed NUMERIC(9) to CHAR(9)
  dependent_name VARCHAR(10) NOT NULL, -- Changed CHAR to VARCHAR
  sex CHAR(1) NOT NULL,
  bdate DATE NOT NULL,
  relationship VARCHAR(30) NOT NULL, -- Changed CHAR to VARCHAR
  PRIMARY KEY (essn, dependent_name),
  FOREIGN KEY (essn) REFERENCES employee(ssn)
);

CREATE TABLE dept_locations (
  dnumber INT NOT NULL, -- Changed NUMERIC(1) to INT
  dlocation VARCHAR(15) NOT NULL, -- Changed CHAR to VARCHAR
  PRIMARY KEY (dnumber, dlocation),
  FOREIGN KEY (dnumber) REFERENCES department(dnumber)
);

-- 2. Insert Data (using MySQL syntax: INSERT INTO...VALUES and YYYY-MM-DD dates)

INSERT INTO department VALUES ('Research',5,'333445555','1988-05-22');
INSERT INTO department VALUES ('Administration',4,'987654321','1996-01-01');
INSERT INTO department VALUES ('Headquarters',1,'888665555','1981-06-19'); -- Corrected date from '19=JUN-1981'

INSERT INTO employee VALUES ('John','Smith','123456789','1965-01-09','731 Fondren, Houston TX','M',30000.00,'333445555',5);
INSERT INTO employee VALUES ('Franklin','Wong','333445555','1965-12-08','638 Voss, Houston TX','M',40000.00,'888665555',5);
INSERT INTO employee VALUES ('Alicia','Zelaya','999887777','1968-01-19','3321 Castle, Spring TX','F',25000.00,'987654321',4);
INSERT INTO employee VALUES ('Jennifer','Wallace','987654321','1941-06-20','291 Berry, Bellaire TX','F',43000.00,'888665555',4);
INSERT INTO employee VALUES ('Ramesh','Narayan','666884444','1962-09-15','975 Fire Oak, Humble TX','M',38000.00,'333445555',5);
INSERT INTO employee VALUES ('Joyce','English','453453453','1972-07-31','5631 Rice, Houston TX','F',25000.00,'333445555',5);
INSERT INTO employee VALUES ('Ahmad','Jabbar','987987987','1969-03-29','980 Dallas, Houston TX','M',25000.00,'987654321',4);
INSERT INTO employee VALUES ('James','Borg','888665555','1937-11-10','450 Stone, Houston TX','M',55000.00,NULL,1);

INSERT INTO project VALUES ('ProductX',1,'Bellaire',5);
INSERT INTO project VALUES ('ProductY',2,'Sugarland',5);
INSERT INTO project VALUES ('ProductZ',3,'Houston',5);
INSERT INTO project VALUES ('Computerization',10,'Stafford',4);
INSERT INTO project VALUES ('Reorganization',20,'Houston',1);
INSERT INTO project VALUES ('Newbenefits',30,'Stafford',4);

INSERT INTO works_on VALUES ('123456789',1,32.5);
INSERT INTO works_on VALUES ('123456789',2,7.5);
INSERT INTO works_on VALUES ('666884444',3,40.0);
INSERT INTO works_on VALUES ('453453453',1,20.0);
INSERT INTO works_on VALUES ('453453453',2,20.0);
INSERT INTO works_on VALUES ('333445555',2,10.0);
INSERT INTO works_on VALUES ('333445555',3,10.0);
INSERT INTO works_on VALUES ('333445555',10,10.0);
INSERT INTO works_on VALUES ('333445555',20,10.0);
INSERT INTO works_on VALUES ('999887777',30,30.0);
INSERT INTO works_on VALUES ('999887777',10,10.0);
INSERT INTO works_on VALUES ('987987987',10,35.0);
INSERT INTO works_on VALUES ('987987987',30,5.0);
INSERT INTO works_on VALUES ('987654321',30,20.0);
INSERT INTO works_on VALUES ('987654321',20,15.0);
INSERT INTO works_on VALUES ('888665555',20,NULL);

INSERT INTO dependent VALUES ('333445555','Alice','F','1986-04-04','Daughter');
INSERT INTO dependent VALUES ('333445555','Theodore','M','1983-10-25','Son');
INSERT INTO dependent VALUES ('333445555','Joy','F','1958-05-03','Spouse');
INSERT INTO dependent VALUES ('987654321','Abner','M','1942-02-28','Spouse');
INSERT INTO dependent VALUES ('123456789','Michael','M','1988-01-04','Son');
INSERT INTO dependent VALUES ('123456789','Alice','F','1988-12-30','Daughter');
INSERT INTO dependent VALUES ('123456789','Elizabeth','F','1967-05-05','Spouse');

INSERT INTO dept_locations VALUES (1,'Houston');
INSERT INTO dept_locations VALUES (4,'Stafford');
INSERT INTO dept_locations VALUES (5,'Bellaire');
INSERT INTO dept_locations VALUES (5,'Sugarland');
INSERT INTO dept_locations VALUES (5,'Houston');

-- 3. Alter Tables (Foreign Keys that reference each other)

-- This must be run AFTER the employee table is created and populated, 
-- but it's fine to keep the ADD CONSTRAINT syntax.
ALTER TABLE department
  ADD CONSTRAINT depemp FOREIGN KEY (mgrssn) REFERENCES employee(ssn);

ALTER TABLE employee
  ADD CONSTRAINT empemp FOREIGN KEY (superssn) REFERENCES employee(ssn);