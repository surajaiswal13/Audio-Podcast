# Setting up project and project Environment for Local System 

## 1. create environment
```
$ conda create -n envname python=3.7
```

## 2. Activate your Environment
```
$ conda activate EnvName
```

## 3. Install All Requirenments using requirements.txt

NOTE: goto to the folder when requirements.txt file is present before executing the below command.

```
$ pip install -r requirements.txt
```

## 4. Configure the project

### NOTE: Make sure you are in the main project folder
```
$ python manage.py migrate
```

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```

5. Run the Project on your Local System

```
$ pthon manage.py runserver
```

<!-- ##                OR

# Use Docker Container

```
$ docker-compose up
``` -->

##                 OR

# Use Hosted Application for for Directly accessing Api's
```
$ https://audio-podcast.herokuapp.com/
```

# Urls and api's to Access

## 1. Crearing account 
#### We can use Admin page to Register new user using the existing SuperUser

```
$ https://audio-podcast.herokuapp.com/admin
```
## 2. Logging in User 

#### In Response we get Token and we have to add that token to header for Authentication required Operations

Method = POST
```
$ https://audio-podcast.herokuapp.com/login/
```
Example Input: 
{
    "username":"sam",
    "password":"sam123"
}

Reponse: Token Value

## 2. Logging out User 

#### In Response we get Token and we have to add that token to header for Authentication required Operations
Method = POST
```
$ https://audio-podcast.herokuapp.com/logout/
```

## Setup up Header for Accessing the Api's

NOTE: We have used Token Authentication that is why we need to set Authentication in header
NOTE: Only active and admin user will be able to access the api's as per the requirement

In Postman, Get into header section and add "key" as "Authorization" and "value" as "Token token_value_dscdncnd" which we get from logging in [i.e Step 2] as Response 

In some cases, we also need to add "key" as "content-type" and "value" as "json/application" in header

## Api's for Shows

### 1. Api for Creation of Show.

#### For creating a show
Method = POST
```
$ https://audio-podcast.herokuapp.com/show/create/
```

## 2. Api for Listing all Shows

#### It will list all shows present in the database
Method = GET
```
$ https://audio-podcast.herokuapp.com/show/view/all
```

## 3. Api for Updating an particular show

#### It is used for Updating the details of a particular show
Method = PUT
```
$ https://audio-podcast.herokuapp.com/show/update/<slug:slug>/
```

## 4. Fetch details of a particukar show

#### View details of a particular show using slug
Method = GET
```
$ https://audio-podcast.herokuapp.com/show/view/<slug:slug>
```

## 5. Api for Deleting a Show

#### Deleting a show using its slug
Method = GET
```
$ https://audio-podcast.herokuapp.com/show/delete/<slug:slug>
```

## Api's for Episodes

### 1. Api for Creation of Episode.

#### For creating a episode
Method = POST
```
$ https://audio-podcast.herokuapp.com/episode/create/
```

## 2. Api for Listing all episodes

#### It will list all shows present in the database
Method = GET
```
$ https://audio-podcast.herokuapp.com/episode/view/all
```

## 3. Api for Updating an particular episode

#### It is used for Updating the details of a particular episode
Method = PUT
```
$ https://audio-podcast.herokuapp.com/episode/update/<slug:slug>
```

## 4. Fetch details of a particukar episode

#### View details of a particular episode using slug
Method = GET
```
$ https://audio-podcast.herokuapp.com/episode/view/<slug:slug>
```

## 5. Api for Deleting a episode

#### Deleting a episode using its skug
Method = DELETE
```
$ https://audio-podcast.herokuapp.com/episode/delete/<slug:slug>
```

## 6. Api for Fetcing all episodes related to a show

#### Deleting a episode using its skug
Method = GET
```
$ https://audio-podcast.herokuapp.com/episode/show/<slug:slug>
```
Where slug = Show api slug we can get it by list all shows and looking into detail we will be able to see the slug part

NOTE: Implemented Extra Api's as per the bonus requirements

NOTE: Celery implementation, Dockerization and CLoud Database implementation in progress

NOTE: Use form-data under body section for input

NOTE: For Example Inputs Check out "Audio Podcat.postman_collection.json" file it is a collection of postman testcases on Audio Podcast project

## Contributors <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25> 

- Suraj Jaiswal