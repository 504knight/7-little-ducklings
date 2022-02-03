# Odd Jobs Web App

## Project Overview

The Odd Jobs Web App aims to help Customers find people to do Odd Jobs on their property by pairing Workers with each job. The system will take job listings from the Customers and display them to Workers. Then Workers will select the jobs. Priority will be given to the Workers with highest reviews. Workers will be charged a 10% fee that is supplied to the Owner and be left with 90% of their profits.

## Team Organization

Project Manager: Logan Ballard (may change over the course of the project)

Designers and Developers: Alexander Hardy, Matt Scribner, James Slade

## Software Development Process

The development will be broken up into five phases. Each phase will be a little like a Sprint in an Agile method and a little like an iteration in a Spiral process. Specifically, each phase will be like a Sprint, in that work to be done will be organized into small tasks, placed into a “backlog”, and prioritized. Then, using on time-box scheduling, the team will decide which tasks the phase (Sprint) will address. The team will use a Scrum Board to keep track of tasks in the backlog, those that will be part of the current Sprint, those in progress, and those that are done.

Each phase will also be a little like an iteration in a Spiral process, in that each phase will include some risk analysis and that any development activity (requirements capture, analysis, design, implementation, etc.) can be done during any phase. Early phases will focus on understanding (requirements capture and analysis) and subsequent phases will focus on design and implementation. Each phase will include a retrospective.

| Phase | Iteration |
| :-----: | :-----: |
| 1 | Requirements Capture |
| 2 | Analysis, Architectural, UI, and DB Design |
| 3 | Implementation and Unit Testing |
| 4 | More Implementation and Testing |

We will use Unified Modeling Language (UML) to document user goals, structural concepts, component interactions, and behaviors.

## Communication Policies, Procedures, and Tools

### Policies

- Maintain consistent communication with the team through discord and in person meetings.
- @everyone in Discord when you submit a pull request so it can be reviewed by others before being merged.
- Comment on parts of pull requests when you see an error or something needs revising.

### Procedures

In person meetings will be held Mondays and Wednesdays in a Library Study Room at 11:30 am. If a team member cannot make it to a meeting in person they will join via the Discord Stand-up voice channel. If that is not possible then it must be communicated with the other team members.

To begin meetings each individual will talk about what they are working on. They will describe successes first and then discuss challenges with the rest of the group.

When brainstorming sessions are needed every individual will write down ideas on sticky notes such that others cannot see their ideas. Then, they will all be discussed and decided upon. This way we preserve creativity within our team.

### Tools

Discord - Main mode of communication. Individual text channels for each Project Milestone and a Stand-up Room voice channel.

GitHub - Formal repository used for submissions, version control, data tracking, and communication with Professor Dan Watson and TA Rob Johnson. GitHub Projects is used as an Agile Sprint board with a Kanban template. The Project boards allow projects to be tracked easily, and big concepts to be broken down into a list of Todos for each sprint.


## Risk Analysis

- Database Structure
	- Likelihood - Low
	- Severity - Very High
	- Consequences - Ineffective models for data lead to complicated code that may result in poor workarounds. Accessing balances, tranactions, account info, reviews, etc. would end up confusing.
	- Work-Around - None. The system will not function properly without correct database implementation. It is necessary to store information about the customers, workers, jobs, etc.
- Login
	- Likelihood - Low
	- Severity - Medium
	- Consequences - Poor customer experience getting into the application or signing up for the first time.
	- Work-Around - None. This is a necessary part of the application due to security and account types.
- Funds Exchange
	- Likelihood - Low
	- Severity - High
	- Consequences - Incorrect amounts being transferred due to unclear or improperly implemented code.
	- Work-Around - None.
- User Interface
	- Likelihood - Low
	- Severity - Very High
	- Consequences - Frustrating experience interacting with the application and performing desired actions. Could become too complex and hard to find all the options frequently used.
- Hosting
	- Likelihood - Low
	- Severity - Medium
	- Consequences - System will not be able to be access information from the database or be accessed by the user.
	- Work-Around - Host system through a hosting service.

## Configuration Management

See the README.md in the Git repository.

