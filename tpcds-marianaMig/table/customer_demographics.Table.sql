
CREATE TABLE tpcds.customer_demographics (
    cd_demo_sk INT NOT NULL,
    cd_gender CHAR(1),
    cd_marital_status CHAR(1),
    cd_education_status STRING,
    cd_purchase_estimate INT,
    cd_credit_rating STRING,
    cd_dep_count INT,
    cd_dep_employed_count INT,
    cd_dep_college_count INT,
    PRIMARY KEY (cd_demo_sk)
) USING DELTA;

