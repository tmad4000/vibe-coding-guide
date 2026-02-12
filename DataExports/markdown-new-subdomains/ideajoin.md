# Ideajoin

Ideaflow / IdeaJoin.com Collaborative Ideation Platform Introduction
a platform to collaboratively build graphs  -- of ideas, knowledge, and people -- to support individual and collaborative research, creativity, synthesis, and analysis
[Or:
-a “shared exo-brain”
-a “gestalt processing system](https://drive.google.com/file/d/0B-pHhDIV_JyBbU54ZDdRSENhbEk/edit?usp=sharing)” for society
-a collaborative network of human ideas and intentions
Which, incidentally, provides key data AIs are lacking -- as creative human thinking is rooted in human experience.
[(seeking additional research project or paid full time collaborator great at frontend Javascript or NLP/ML. Funding offer from billionaire Nicolas Berggruen](http://en.wikipedia.org/wiki/Nicolas_Berggruen); See below)
[[a]](#cmnt1)
## Demos
[jcr.stcatz.ox.ac.uk/ideas/](http://jcr.stcatz.ox.ac.uk/ideas/)Sample user base: St. Catherine’s College Oxford
[[[[Graph view](http://instadefine.com/IdeaOverflow/Outlinr-PHP/public_html/ideabox_catzjcr/public_html/index.1.7_suggestionbox_graph.php?mapid=80)[b]](#cmnt2)[c]](#cmnt3)[d]](#cmnt4)(refresh page once after load if necessary)
[ideajoin.com](http://ideajoin.com/)Homepage/create a suggestion box.
2000+ users.
Oxford colleges amended constitutions to require use
[Graph of MIT 100k Entrepreneurship Contest Semifinalists](http://mit100k.ideaboard.jacobcole.net)
[HackathonIdeas.tk](http://hackathonideas.tk)

Commercial Product (data analysis platform)
[Bleeding edge: ideaflow.mjgil.com](http://ideaflow.mjgil.com)

[Updated: 1/27/2015 Jacob Cole <jcole@mit.edu](mailto:jcole@mit.edu)>
Advisers: Prof. Tim Berners-Lee, Henry Lieberman
[More info: index.ideajoin.jacobcole.net , ideaflowproject.wordpress.com](http://ideaflowproject.wordpress.com/)

## Table of Contents
- [Demos](#h.ig8au4yanpy)
- [Table of Contents](#h.7i8ox0l2xlzk)

- [Abstract](#h.7n2ikct0gsc)

- [Status (1/22/2015)](#h.qwjc236tv9ny)
- [Seeking further full-time/research project-level collaborators](#h.p5hguf5f16o1)

- [Current](#h.1lqozbo1xb2j)

- [Users](#h.7omotwr5zn45)
- [Customers](#h.i9cf0clvo49i)

- [About:](#h.r8epakqq376d)

- [Learn how IdeaFlow works, via use case as a suggestion box platform for governments:](#h.w3c9x6pz0qf)
- [A practical realization of the vision of Semantic Web/The Giant Global Graph](#h.qzrybaxupfql)
- [User case study: St Catherine’s College Oxford](#h.b7e40ihb6rq9)

- [Motivations](#h.yqd6hrk6krjn)
- [Commercial Product:](#h.32u0bnaw7648)

- [1. Data Analysis Platform](#h.4v6cm3q23bnn)
- [2. “Project dashboard” for large businesses and academic institutions](#h.esrultlhvtw)

- [Near-Future plans:](#h.g3xa827h0kfo)

- [Smart notetaking software: Make the best ever application to keep lists of ideas + new interface for posting to the Web.](#h.ytybjjmoth07)

# [[[Abstract[e]](#cmnt5)[f]](#cmnt6)[g]](#cmnt7)
[At the core, IdeaFlow is a web platform  that enables individuals or groups of people to create “ideation boards” on which they can post partially or fully formed ideas/projects and share connections they see between them or external ideas/projects. To facilitate the task of finding related ideas, IdeaFlow has machine learning/natural language processing algorithms to automatically suggest connections between ideas, and an interface to visualize networks of ideas. Because finding relationships between ideas is such a fundamental operation of cognition, this platform is applicable across fields, from organizing and exploring ideas/projects within a company or research group, to identifying clusters of suggestions from a political constituency, to finding patterns in spreadsheets of textual data. Ultimately, IdeaFlow has the goal of realizing my advisor Prof. Tim Berners-Lee's vision of creating a unified Giant Global Graph http://en.wikipedia.org/wiki/Giant_Global_Graph of ideas which exhibits emergent intelligent properties. To understand the platform better, let’s consider a specific use case (below: Learn How IdeaFlow Works](#h.r8epakqq376d)).

## Status (3/1/2017)

## Hiring full time full stack Web developer (React, Redux, Node) and mobile developer

## Status (1/22/2015)

### [Seeking further full-time /research project](http://research.ideajoin.jacobcole.net)-level collaborators
Especially needed skills are: hardcore webdev; hardcore ML/NLP.  Web technologies include ReactJS, Backbone, D3, and NodeJS; Python for machine learning/NLP

If you or anyone ideal you know would like to be involved on a lower time-commitment scale, like undergraduate research, we may be able to arrange that as well.

### Users
Beta Launched for Oxford University January 26, 2014
[3,838 Unique users, 20,319 Hits, (58.2% returning). 4232 contributions [1]](#ftnt1)

[2 Oxford colleges amended student government constitutions to require VP to respond to suggestions in system[2]](#ftnt2)

### Customers
[Customer Charter Partners insurance company currently paying $500/mo to use our alpha platform to find patterns within the thousands of claims they process so as find how to prevent them. See below](#h.32u0bnaw7648)

# About:

## Learn how IdeaFlow works, via use case as a suggestion box platform for governments:
Right now, people make suggestions to politicians by writing letters. But we rarely know when, or if, our letters have been read, nor do we know if our suggestions have been acted upon or merely forgotten. We also don't have a way to find or support others who have written similar letters. Thirdly, there's no central place we can go online to see all of the initiatives government has actually passed in a certain time period, which is the core of transparency.

[These were problems faced by St. Catherine's College, Oxford student government, and, last term, with the support of collegemates David Furlong and Chris Casson, I created and implemented a website that helps solve all of them at once: http://jcr.stcatz.ox.ac.uk/ideas/](http://jcr.stcatz.ox.ac.uk/ideas/). It takes the form of a high-tech suggestion box website, and is a new medium for citizens and governments to communicate, and for transparency.

The website allows students to post complaints, ideas, and suggestions to be acted upon by the JCR committee (undergraduate student government) and see whether they've been acknowledged, if they're in progress, if they're done, or rejected. The website became so popular that a motion was passed requiring the VP of the JCR to weekly review suggestions submitted, mark them as acknowledged, in progress, or done as appropriate, and, where reasonable, take the next step to turn them into a motion. Passed motions are presented as completed suggestions.

[Finally, and most importantly, as users type in suggestions, the existing list of suggestions is searched in real-time to find related suggestions. A Graph view](http://instadefine.com/IdeaOverflow/Outlinr-PHP/public_html/ideabox_catzjcr/public_html/index.1.7_suggestionbox_graph.php?mapid=80) enables users to visualize how suggestions cluster and note relationships between suggestions they find (Refresh the page once after loading). The more relationships people note manually, the better the automatic relationships-finding algorithm can function.  Loading the relations between ideas that users have separately in their own heads into a giant global graph enables people who hold the pieces to each other's puzzles to find each other.. Additionally, clustering related suggestions helps users to identify and address the root cause behind them,and to come up with more creative solutions.

As an example, consider the following suggestions which were submitted separately:
1) Leftover foods given to students rather than bins
2) Leftover food donated to homeless shelters
3) Less Hall waste #eco
4) Leftover food composted
5) Make online hall sign-up include dietary requirements (i.e. dairy/gluten-free)

A user of the system noted the connection between 1, 2. Another user noted the connection between 2 and 4. The matching algorithm suggested to another user that “Less Hall waste #eco” should be connected to this cluster as well, and a user confirmed the connection. Aggregating the ideas strengthened and deepened the discussion by helping students with similar causes come together and promoting them to ponder the deeper root cause behind these related issues. This provided a basis for them to produce creative ideas that address it, such as: “Make online hall sign-up include dietary requirements (i.e. dairy/gluten-free)”

## A practical realization of the vision of Semantic Web/The Giant Global Graph
[As a final comment, one of the larger reasons this project is exciting to me is because it's a step towards realizing what I think is perhaps the most significant potentials of semantic web, which I didn't properly come to understand until this year while UROPing at the W3C with Tim Berners-Lee: building the Giant Global Graph http://en.wikipedia.org/wiki/Giant_Global_Graph](http://en.wikipedia.org/wiki/Giant_Global_Graph) of ideas. The bulk of meaningful content we write -- articles, academic papers, etc. -- entail expressing the relationships between ideas. But right now these connections sit in unstructured text. Thus:

Alice might have a connection between idea A and Idea B in her head
Bob might have a connection between idea B  and idea C in his head

But right now, the transitive connection between ideas A, B, and C can only be discovered if Alice and Bob happen to have a conversation, or stumble upon another’s writings!

Creating a platform that encourages users to contribute connections between ideas in a way that’s explicit enables us to load connections between ideas that are in everyone's separate notes/writings into a central graph. This enables users to discover all the ideas related to their ideas from amongst an entire group of people. Moreover, the more connections there are, the better the recommendation algorithm can suggest new connections. Facebook’s “People you may know” feature, which is based largely on mutual friends, is the very tip of this much larger iceberg of graph-based recommendation algorithms. IdeaFlow, seeks to be Facebook for ideas themselves to socialize with each other (of course, through the substrates of their human hosts).

## User case study: St Catherine’s College Oxford
The suggestion box for St. Catherine’s College, Oxford has already proven to be remarkably useful despite the early stage of software development. And happily, the suggestion box itself allows users to make recommendations to further develop and refine the software..

[A suggestion box for St. Catherine’s College Oxford launched publically at jcr.stcatz.ox.ac.uk](http://jcr.stcatz.ox.ac.uk/) on Jan 26, 2014 and by June 6, 2014 had received significant usage: 106 suggestions, 127 comments, and 1245 upvotes.   Additionally, the suggestion box system was so well-liked that the undergraduate student government (JCR Committee) amended its constitution to require the Vice President to review suggestions, mark them as acknowledged, in progress, done, or, in rare occasions, rejected, and propose new motions based off of them as appropriate.

88 of these suggestions have been acknowledged by student government, 8 are in progress being implemented, 3 have been completed, and 4 have been rejected.

Examples of implemented suggestions include:
- Radio or speakers you can plug iPod into in gym
- Add what vegetables/sides/carbs will be at hall, for those of us who are less meat fussy and more veg fussy.

Suggestions in progress include
- Unify ALL the logins so we don't have to memorise 36 different user names and passwords

Other colleges have adopted the platform as well, and the president of Oxford University student government (OUSU) proposed an analogous motion to be passed first thing next term for student government as a whole in the hope that it will help enable the much-criticized organization to become more transparent and to better respond to student feedback.

[Anyone can make a suggestion box at our homepage, ideajoin. com](http://ideajoin.com/) .

# Motivations
What motivates me is right now I see the most fundamental pressing problem in the world is that human activity is scattered:
[People with synergistic ideas in research groups, big companies, and society aren't aware of each other (Tim Berners-Lee says "There are millions of scientists trying to cure the likes of AIDS and Alzheimer's. Maybe the cure is currently separated in different people's heads. How can we design the web so that these half-formed solutions can come together How can we build a really creative space for scientists](http://www.wired.co.uk/news/archive/2011-02/01/cancer-commons)?" in
http://www.wired.co.uk/news/archive/2011-04/19/tim-berners-lee-science-w3c). Talented people start redundant or non meaningful startups even when there are many great ideas available low-hanging.
News media has a short attention span; we hear about bombings in Syria and earthquakes in Haiti one week and something else the next, even if the problems aren't resolved. Resultingly, the well-being of suffering people is at the mercy of what entertains the first world.
This isn't okay.

Minsky teaches us that a mind is a system to meditate between a collection of little agents, and that society is a mind. This mind is currently scatterbrained.

[In the abstract, the goal of this project is to build a "gestalt processing system for society" (ref: ideajoin.jacobcole.net ) so that everyone, everywhere can be included in the circle of humanity. It is to lift the fog of non connection that sits on the world between people and their ideas,  and build the giant global graph. It is to create a system to relate ideas - a rudimentary intelligence able to, for fundamental reasons, make broader connections than any single brain - which, as a side effect, produces a new paradigm for conducting Internet research that is fundamentally better than Google for many tasks (ref: researchlists.jacobcole.net](http://researchlists.jacobcole.net)). It also incidentally produces a new type of smart text document not trapped in the paradigm of paper.

The data collected from this system is vast and hopes to lay the groundwork for strong AI that produces new ideas autonomously.

(A second problem I see is that many of the smartest people I know spend their days working to improve the ad recommendation system on Facebook instead of curing cancer or building strong AI. I am striving to give these people a materially equally appealing or more appealing alternative option that also gives them an opportunity to directly help people!))

# Commercial Product:

## 1. Data Analysis Platform
Web platform that enables groups to collaboratively build graph-structured knowledge bases to discover patterns in data better than any individual. People in an organization upload  spreadsheets, and then note connections they see between the entries (e.g. Insurance claims). NLP/ML algorithms suggest further connections which humans confirm. Patterns emerge.The
Customer Charter Partners insurance company currently paying $500/mo to use our alpha platform to find patterns within the thousands of claims they process so as find how to prevent them
[Demo of this instance: ideaflowy3.meteor.com](http://ideaflowy3.meteor.com)

[Competitors:
Organizations use  http://keylines.com/](http://keylines.com/) to visualize and explore graph-structured data they already have (similar to Palantir’s Project Gotham). It’s great at this. However, beyond Keylines, by allowing users to add new connections, IdeaFlow enables organizations to actually create new graph-structured data from previously flat data too!

## 2. “Project dashboard” for large businesses and academic institutions
IdeaFlow can be applied to a large organization to create a central, graph-structured dashboard of all the projects and ideas present within that organization.  Large businesses and academic institutions have many projects going on within. Often, people in different parts of these organizations have related or synergistic ideas/projects, and yet are not aware of each other. Currently, there is no standard software to build databases of projects within companies, much less ideas. Present partial solutions consist of central wikis (for instance, within Palantir) and HTML pages (for instance, within MIT). However, these are a) too difficult to update with regularity, b) provide no means for users to note new connections between ideas.

 IdeaFlow seeks to close the gap between personal notetaking and idea/project sharing. IdeaFlow is working to build a better alternative to the above ad hoc systems by providing an easy-to-use platform for members of an organization to share, explore, and note connections they notice between projects and ideas going on within that organization (and to those in the larger world). User discovery of connections is supported by natural language processing/artificial intelligence algorithms that suggest related ideas.

# Near-Future plans:

## Smart notetaking software: Make the best ever application to keep lists of ideas + new interface for posting to the Web.
[Thoughtstreaming vision thoughtstreaming.jacobcole.net](http://thoughtstreaming.jacobcole.net)

Web app/Mobile app/Client app
Feature outline:
- ability to send ideas written in notes to IdeaFlow suggestion boxes, or other media like Facebook by appending @StCatzOxford, @Shadi, or @MIT, or @facebook .to the note
- ability to note related ideas next to a given idea with <> syntax. Automatically suggested related ideas,
- track completion status of ideas

Vaguely,  “Twitter for ideas” with idea relations, status tracking, and privacy by default
“Smart text editor” alternative to Evernote.com and Workflowy.com.

Alternative formulation: Collaborative ideation and team formation for hackathons
Alternative formulation: Building an online platform to help with collaborative ideation and team formation for hackathons.  

Problem:
Both computer programming competitions (hackathons) and project classes require participants to conceive and implement creative ideas within a limited time frame. Many people devote tremendous effort to projects that don’t inspire them, even while there is a wealth of killer ideas to go around. People who could be ideal collaborators or have deeply synergistic ideas pass in the hall without knowing it. Right now, within our university, and in the larger world, we often hold the pieces to each other's puzzles without knowing it.

[At the same time, tons of people keep lists of ideas, but they are scattered, as there's no ideal software for recording, organizing and sharing brainstorms that can appear unpredictably at any time. The MIT computing club SIPB’s own slightly out of date list is an example of this https://sipb.mit.edu/projects/ideas/](https://sipb.mit.edu/projects/ideas/)
[Prof. Seth Teller’s random ideas pages is anotherhttp://people.csail.mit.edu/teller/misc/randomideas.html](http://people.csail.mit.edu/teller/misc/randomideas.html)

Solution
Specifically, IdeaFlow entails creating a place online where people can post ideas they have for projects, note related ideas to a given idea when they find them, and use this data to train algorithms to automatically suggest more related ideas (the latter is the subject of some of my research). Equally important is creating a simple visual interface for people to explore these knowledge graphs. This fits within the purview of the specs discussed above.

[[1]](#ftnt_ref1)318 Ideation Boxes Created, 1240 ideas, 577 connections between suggestions/Ideas, 2097 Upvotes
[[[2]](#ftnt_ref2) St. Catherine’s College jcr.stcatz.ox.ac.uk/ideas/, and St. Edmund’s Hall (Teddy Hall), www.teddyhall.co.uk/suggestions.html](http://www.teddyhall.co.uk/suggestions.html). Teddy Hall’s amendment is provisional, To be confirmed in December 2014.
[[a]](#cmnt_ref1)Hi! I'm interested in learning more about your company. Please reach me at magnifyscience@gmail.com . Thanks!
[[b]](#cmnt_ref2)The moving graph is pretty distracting and I can't think of any clear reason it needs to move.

I also think it'd be nice to be able to expand the nodes in the graph - the short descriptions attached to nodes aren't really enough information

I think this graph could potentially be very useful, but I'm not clear on how you imagine this being used right now.
[[c]](#cmnt_ref3)UI is a prototype and needs much improvement; the snippets of text should be visible. The importance of the graph is to enable us to view clusters of related ideas so that we can deepen the discussion. Furthermore, adding connections to the graph collaboratively and suggesting new connections of algorithms allows people to find connections they never would have on their own.
[[d]](#cmnt_ref4)Hi
[[e]](#cmnt_ref5)I think this sounds very academic - it's very interesting to me, but I don't think it would catch the attention of somebody else (e.g. if we hadn't already talked about this). I like the example of how people would actually use this more as an introduction than writing in the abstract about what it does.
[[f]](#cmnt_ref6)Is this edit better?
[[g]](#cmnt_ref7)It's better - but still a bit hard to follow. Let's say you had to give an elevator pitch for ideaJoin - what would that say?

I'm not saying that an abstract is an elevator pitch - but theres a pitch element here thats kind of missing.

"IdeaJoin is a to-do list/idea board/suggestion box that automatically finds potential collaborators and synergies."