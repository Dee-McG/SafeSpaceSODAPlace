![SafeSpaceSODAPlace Logo](static/img/ss-full-logo.png)

SafeSpaceSODAPlace is a user based discussion board where people can discuss accessibilty issues that they may be facing in the work place. All discussions and user inputs are anonymous which gives people peace of mind. 

Users will be able to draw attention to their own needs that may not be being met in the work place without having to directly disclose any hidden disabilities that they woud rather keep private. 

You can find the live site [here](https://safe-space-soda-place.herokuapp.com/).

## Wireframes
[Click here for the desktop wireframe](static/img/readme/full-wireframes.png)

## Flow

![Site flow chart](static/img/readme/hackathon-flow.png)

## Features
- Nav bar that updates depending on user authentication
   - If User not logged in:

![Navbar](static/img/readme/features/01-nav-02.PNG)

   - If user logged in:

![Navbar](static/img/readme/features/01-nav-01.PNG)

- User can register an account

![register](static/img/readme/features/02-register.PNG)

- User can add, edit and view profile information

![profile info](static/img/readme/features/05-profile-info.PNG)

- User can Log in & Log out

![log in](static/img/readme/features/03-signin.PNG)

![log out](static/img/readme/features/03-signout.PNG)

- Messages displayed to update user on any actions happening

![messages](static/img/readme/features/04-messages.PNG)
- User can create a dicussion board

![idea id create](static/img/readme/features/06-make-discussion-board.PNG)

- User can submit an idea to be discussed

![start idea](static/img/readme/features/07-start-ideas.PNG)

- User can add coments to a discussion

![discuss idea](static/img/readme/features/07-discuss-idea.PNG)

![comment on idea](static/img/readme/features/07-comment-on-idea.PNG)

## Testing

### Testing performed on ensure home page renders

* Step 1 - Navigate to [Home Page](https://safe-space-soda-place.herokuapp.com)

**Expected:**<br>
Home Page displayed

**Actual:**<br>
Home Page displayed

### Testing performed on nav bars to ensure they redirect to the correct pages

* Step 1 - Navigate to [Home Page](https://safe-space-soda-place.herokuapp.com)
* Step 2 - Click on nav item and ensure it navigates to the correct page

**Expected:**<br>
All links navigate to the correct pages

**Actual:**<br>
All links navigate to the correct pages

### Testing performed on authentication to ensure users can sign up

* Step 1 - Navigate to [Sign up Page](https://safe-space-soda-place.herokuapp.com/accounts/login/)
* Step 2 - Fill in email, username and password fields
* Step 3 - Submit form

**Expected:**<br>
User can sign in with new details

**Actual:**<br>
User can sign in with new details

### Testing performed on profile page works as expected

* Step 1 - Navigate to [Profile Page](https://safe-space-soda-place.herokuapp.com/profile/username/)

**Expected:**<br>
Profile Page displayed

**Actual:**<br>
Profile Page displayed

### Testing performed on edit profile page works as expected

* Step 1 - Navigate to [Profile Page](https://safe-space-soda-place.herokuapp.com/profile/username/)
* Step 2 - Click edit profile
* Step 3 - Fill in edit profile form and submit

**Expected:**<br>
Profile is updated and user is redirected to their profile

**Actual:**<br>
Profile is updated and user is redirected to their profile

### Testing performed on board creation

* Step 1 - Navigate to [Profile Page](https://safe-space-soda-place.herokuapp.com/profile/username/)
* Step 2 - Enter details into board creation input
* Step 3 - Click create board

**Expected:**<br>
Ideas board is created

**Actual:**<br>
Ideas board is created

### Testing performed on idea submission

* Step 1 - Navigate to [Ideas Page](https://safe-space-soda-place.herokuapp.com/ideas/board/board_no/)
* Step 2 - Fill in form to add an idea and submit

**Expected:**<br>
Ideas added to board

**Actual:**<br>
Ideas added to board

### Testing performed on discussion creation

* Step 1 - Navigate to [Ideas Page](https://safe-space-soda-place.herokuapp.com/ideas/board/board_no/)
* Step 2 - Click start discussion
* Step 3 - Click the discussions page nav link

**Expected:**<br>
Discussion board populated with ideas

**Actual:**<br>
Discussion board populated with ideas

### Testing performed on discussion comment creation

* Step 1 - Navigate to [Discussion Page](https://safe-space-soda-place.herokuapp.com/discussion/)
* Step 2 - Click the comment button to display the comment input box
* Step 3 - Add a comment into the input box and then click submit comment button

**Expected:**<br>
Comment added under correct discussion item

**Actual:**<br>
Comment added under correct discussion item

## Technologies Used

## Contributors

- [Matt Cooper](https://github.com/YesCoops)
- [Steven Dawson](https://github.com/Steven-Dawson18)
- [Django Heimgartner](https://github.com/D1ang)
- [Daisy McGirr](https://github.com/Daisy-McG)
- [Amy O'Shea](https://github.com/AmyOShea)
