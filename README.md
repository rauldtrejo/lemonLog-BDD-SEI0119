# lemonLog-BDD-SEI0119
# Lemon Log

Lemon Log is a technology review site, where authors of the site can write and publish posts and users of the site can comment on articles. The site allows all users to view and explore home page and about page, but only logged in users (users with an account) can create, edit and delete their own comments. 

https://lemonlogbdd.herokuapp.com/

## Screenshots


## Technologies Used
- Python
- PostgreSQL
- Django
- CSS
- Materialize
- Uploadcare
- VSCode
- GitHub
- Google Chrome Developer Tools

## User Stories
The user stories were provided by the client and organized by sprints, see the user stories full description [here.](https://git.generalassemb.ly/wc-sei-0119/project-3-django-client-project/blob/master/user-stories-tech-review.md)

This project covers the first 3 prints and the following bonuses:

### Sprint 1: Basic Auth & Profiles Bonuses
A user should be able to:
- See a "default" profile photo on their profile page before adding their own photo.
- Update their profile photo via Uploadcare.
- See their profile photo next to their posts.

### Sprint 2: CRUD Bonuses:
A user should be able to:
- Visit review pages via pretty urls, like "/reviews/iphone-x".
- Visit user profile pages via pretty urls, like "/users/james".
- On the homepage: 
    - See review content truncated to 1000 characters max, with a link to view more.
    - See a relative published date, e.g. "2 days ago".
    -
### Sprint 3: Validations & Authorization Bonuses:
A user should be able to:
- View an error message when form validations fail:
    - Content must not be empty.
- See a list of review titles they've contributed comments to, on their public profile.
- See the number of comments they've written for each review.

## Data Models (ERD)
![ERD](https://trello-attachments.s3.amazonaws.com/604fce17ff74031564d6dc8a/933x703/17449f828e34d113e4ed59d6ac47be8c/Screenshot_from_2021-03-15_14-13-40.png)



## Wireframes
The following wireframe was created to supplement the the initial wireframes provided by the [client](https://git.generalassemb.ly/wc-sei-0119/project-3-django-client-project/tree/master/tech-review-wrieframes). 

Profile Page

![Profile Page](https://trello-attachments.s3.amazonaws.com/604eacc2f1ce031c5101d081/1060x715/4cca0a1e8653815863c931cd2b1e1123/Profile_V2.png)

## Major Hurdles
- Adding a third party app as uploadcare to allow the user to upload photos to the profile was relatively easy but figuring out how to retrieve one photo from the database to display it in the profile and reviews/comments page required major debugging. 
- 

## Major Victories
- Achieving full CRUD functionality 




## Future Features

- App would have full responsiveness for very small mobiles and tablets. 
