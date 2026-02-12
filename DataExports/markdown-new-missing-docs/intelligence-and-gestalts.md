# Intelligence And Gestalts

Cole, Lee
{Prof. Marvin Minsky
6.868 Society of Mind
31 May 2013

IdeaOverflow IDE (Idea Development Environment) Idea Matching Algorithm
The basis for a platform for collaborative ideation and project sharing.
Jacob Cole, Holden Lee

[Abstract](#h.78840bwr71w2)
[1 A new Turing Test](#h.l1noijd2cnbs)
[Philosophical underpinnings](#h.9cbid28uubcw)
[2 IdeaOverflow finds related ideas](#h.79uec4x3ahwd)
[2.1 Current state of the interface](#h.nojgck4knu7s)
[2.2 Human approaches to linking ideas](#h.pszu429nqsw3)
[2.3 Implementation](#h.88rfgd7yh6du)
[2.4 Results](#h.shj4ro3ir9p6)
[2.5 Future work](#h.cbwvwxu9jwy2)
[3 IdeaOverflow enables societal collaboration](#h.ezaiivx4438b)
[3.1 Philosophical underpinnings: Gestalt theory](#h.pjfhk6ksymo2)
[3.2 Case study: How did “FoodMom” app idea develop?](#h.cznes24zpha)
[Works Cited](#h.pmyvp5vx43ok)
[Appendix: Source Code](#h.5k7kc3w1t26p)

[A MindMap of this paper is available at http://app.wisemapping.com/c/maps/124943/public . The matching algorithm is available at https://github.com/tmad4000/IdeaOverflow_som and the web platform source code is available at https://github.com/tmad4000/ideaoverflow-hackny . A demo of the web app is available at http://pacific-tundra-3629.herokuapp.com/ or (old) http://agile-ocean-3244.herokuapp.com/](http://agile-ocean-3244.herokuapp.com/).

# Abstract

While the Internet currently has many tools to facilitate discussion of people and events, there is no centralized platform optimized to facilitate deep, collaborative thinking.Thus we started IdeaOverflow Idea Development Environment (IDE), an online system that facilitates collaborative cognition by, as a key feature, finding relationships between ideas inputted into a database.

First, we contend that IdeaOverflow is a relevant, modern frame for the problem of strong artificial intelligence that refines the antiquated Turing test, and makes actionable Douglas Hofstadter’s theory that analogy is the core of cognition.

[Second, we develop and apply theories of how humans make connections between ideas and use existing tools (MIT ConceptNet) to take the first steps towards implementing an idea-connection machine. We built a basic web platform, implemented two rudimentary algorithms that find conceptually related ideas, and we lay a road map forward. Even at this early stage, our algorithm often successfully makes relevant connections between ideas drawn from hackathonprojects.tk](http://hackathonprojects.tk/), a public, crowdsourced database of over 100 startup company/hackathon project ideas.

Finally, in Section 3, we apply gestalt theory in a novel way to understand how individuals come up with ideas and apply this understanding to project the process of ideation into a shared space. We demonstrate how the platform as a whole can be used to create new good ideas.

# 1 A new Turing Test

The great difficulty in pushing ideation into a shared space isthat people can only make connections between the ideas in their own minds. The ability to make these connections is a fundamental aspect of human intelligence. Talking to a friend working on a certain idea, a person can suggest related ideas and people that the collaborator should investigate. However, currently, when those ideas are stored in an external database rather than a single person’s mind, this ability to make connections is lost; static databases are not “intelligent”. As knowledge becomes increasingly distributed, we need to make connections between ideas that are not held in the mind of a single person, or even the minds within a personal network.

We propose the following task as an alternative to the Turing Test: program an AI to emulate humans’ ability to find ideas related to a given idea. Given a database of ideas and an idea within the database, the program should find the top 10 to 20 ideas related to that idea, so that the resulting list is indistinguishable from that compiled by a team of humans who have spent extensive time evaluating the list for connections. Like a human collaborator, a system that could do this would suggest related ideas and people that a user should investigate. In this way, it could have a genuinely constructive and intelligent "conversation" with its users about the ideas they are working on. Better than any individual human collaborator, it would try to find the top 10 to 20 ideas out of the database of possibly millions, whereas a human can only search on a much more limited data set.

## Philosophical underpinnings

Our formulation of the problem is new, but it is based on existing theories of human intelligence. Firstly, inThe Analogical Mind (Gentner 2001), Hofstadter argues that analogy is the core of cognition. For example, we connect the concepts of a tree’s shadow, the dry region on the lee side of a mountain, and the metaphorical location beside an older, more accomplished sibling, and encode them using the word “shadow.” Moreover, analogy, that is, finding redundancy and creating abstractions, is at the core of data compression; in other words, it is the key to efficiently encoding information. Hutter has proposed that the problem of data compression--for instance, of the text on Wikipedia--is equivalent to strong AI (Hutter 2000). Relatedly, the long-standing “efficient coding hypothesis” in neuroscience posits that creating a maximally parsimonious model of information is a central task of the human brain.

This is exactly what we propose to do, but with ideas that address human problems. A good idea-matching engine has to find abstract relationships and group ideas together in the same way that “shadow” groups several concepts together. The challenge is, of course, that these relationships can be very abstract.

We use analogy in making connections between ideas: knowing what “Instagram” is (a site that allows immediate sharing of photos), we can guess what “Instaquote” is, and conversely, hearing descriptions of both ideas, we would be able to mentally find a relationship between them, and perhaps suggest a similar name for both. Hofstadter and Hutter’s argument hence justifies idea-linking as an alternative to the Turing Test.

Secondly, several authors have proposed that we cannot think of intelligence as nicely encapsulated within a single person’s brain. This justifies our focus on idea-linking between different people. As a starting point, we should realize that cognition of individuals is already distributed (Hollan 2000). As Minsky writes in Society of Mind, “...each brain contains hundreds of different types of machines, interconnected in specific ways which predestine that brain to become a large, diverse society of partially specialized agencies” (Minsky 1988). Given that an individual’s intelligence resides in the way that these agencies of the mind are organized in specific ways, and given the fact that a society of individuals is organized in specific ways, it is natural to suspect that a society can have “intelligence” on a higher level than that of the individual. As Salomon writes, “People think in conjunction and partnership with others and with the help of culturally provided tools and implements” (Salomon 1997).

Given that culturally provided tools are important to intelligence, a society’s “intelligence” should increase with better socio-technical frameworks. An idea-linking system which passes our test would be valuable as it is a tool that emulates an ability of the human mind in a society, hence paving the way towards better collective intelligence.

# 2 IdeaOverflow finds related ideas

## 2.1 Current state of the interface

We developed a web interface for IdeaOverflow that lists submitted ideas with descriptions, related ideas, categorical tags, authors, and number of “likes.” Note that tags and authors are treated the same way as related ideas in the database.

Figure 2.1-1: Sample of IdeaOverflow database entries

In this rudimentary version, a user submitting an idea has to manually establish connections with existing ideas in the database. For instance, the user who submitted CabShare made a connection to Social Ridesharing App. When the user starts typing in the “related ideas” field, the site attempts to autocomplete the text with ideas already in the database using, for now, simple keyword search. The user then clicks on ideas he or she deems to be related.

Figure 2.1-2: Finding related ideas by keyword search

Although a manual idea-linking system is crude, it already takes us partway to our goal: with some human effort, users can identify other ideas similar to theirs and hence collaborate with other users on ideas of mutual interest. (This is actually a nontrivially powerful approach; see Section 2.2 IV.)

We then took the next natural step by creating an algorithm more intelligent than keyword search that automatically finds relationships between ideas. As mentioned, we contend this is a task that frames the problem of strong AI; if we want to create an algorithm that embodies human-like abilities to find connections, we must first understand how humans connect up different ideas.

## 2.2 Human approaches to linking ideas

We give several hypotheses for the way humans link ideas. (There are also non-human approaches for linking ideas that are beyond the scope of this paper, but are also relevant to the study of strong AI.)

I. Matching by related concepts

A simple but relevant and effective approach is to regard an idea as a “bag of concepts,” and consider ideas as related if they have one or more concepts that are related to each other. Relatedness can be evaluated based on graph adjacencies in a commonsense database. For humans, this database is derived by life experience, and for a machine, it can be derived from ConceptNet.

II. Matching by problem/solution

We can refine matching by related concepts if we first understand the components of an idea. An idea has two main components to it.

- A problem it’s trying to solve, or more generally, an open gestalt it’s trying to resolve. An open gestalt is anything that tugs on a person’s attention, and can be hunger, a desire to meet people, an urge to write down an inspiration, and so forth. This is discussed in more detail in Section 3.
- A method of solution, or technology that it utilizes. For instance, does it use crowdsourcing to accomplish something that would take an inordinate amount of time otherwise?

A person makes a connection between two ideas if they are related in either of these components.We can use matching by related concepts on both the components. Splitting ideas into components allows us to compare them more precisely, as well as “mix and match” problems and solutions. Furthermore, after people learn a lot of ideas, they get more of a sense which sorts of techniques are useful for which kinds of problems. They can better see all the techniques that are good for a set of related problems, or alternatively, see all the problems that can be solved by a set of related techniques.

For instance, when asked how he came up with solutions to math and physics problems so easily, Richard Feynman once said that he kept a list of open problems in his head, and a list of solution techniques that he accumulated. Whenever someone told him a problem or technique, he would see whether it matched up with a technique or a problem he already knew. IdeaOverflow seeks to automate this process.

III. Abstraction Hypothesis:

Comparisons are most meaningful at intermediate levels of abstraction. Comparisons at too general of a level are less useful: just because both ideas reference “people” doesn’t mean they are very related. Comparisons at too specific of a level are problematic because ideas rarely match at that level. Thus, when comparing ideas, it makes sense to replace specific concepts in the ideas by their intermediate level hypernyms (categorical abstractions) and compare them at that level.

IV. Matching by Transitivity

If ideas A and B have one or more ideas in common (say C, D, and E), then chances are, ideas A and B are also related. The power of simple matching by transitivity should not be overlooked. Making just a few connections allows a connected graph of ideas to “bootstrap” further connections in a positive feedback loop: one linkage between ideas begets more linkages between ideas. Indeed it is by a similar positive feedback loop that humans acquire an understanding of abstract concepts (as an example of this, dictionaries are built of relations between concepts).

To match ideas in our heads, it is inefficient to search through all the ideas that we have whenever we get a new idea. Instead, only a few memorable ideas, or general categories of ideas, are near the top levels of our mind at any given time. When a new idea A reminds us of another idea C that isn’t particularly memorable, then probably A reminded us of big idea or category B, and C is very related to B. Thus, to efficiently program a way to find related ideas, we can find the categories or prominent ideas related to the idea, and then look for other ideas that fit in that category or are related to the prominent idea. We can hence think of categories as connectors between ideas. Note that an idea can belong to more than one category.

Thinking computationally, the graph of ideas in our minds is most likely sparse, as we can’t hold too many relationships in our mind at the same time. This is not a disadvantage, though, because following a few paths allows us to get to a lot of ideas: Intelligence isn’t just how much is stored in the brain, but also how much one can compute in a given time. For small n, the number of ideas that you can get to from a given idea following the edges of a sparse graph is exponential.

[The grouping together of ideas and categories here is intentional: categories can be treated in the same way as ideas themselves. This is the idea of reification: abstract categories of ideas are made concrete through naming, and become like ideas. Because they are stand-ins for a whole category of ideas, they have the function of compressing the map of ideas within a person’s head. Thus, developing an intelligent taxonomy of ideas not only makes the matching process better (as above), but also makes search efficient (see http://ideamap.tk](http://ideamap.tk) for an example).

V. Story Hypothesis:

Finally, we point out peopleuse story understanding(as described in Winston) to recognize relationships between different ideas: An idea gives a solution to an existing problem, or “closes an open gestalt,” and a cause/effect or process/goal is the simplest kind of story. For example, we understand crowdsourcing as the category of ideas where an activity that is not hard but takes a lot of time is made doable by distributing the effort among a large number of users.

## 2.3 Implementation

The first idea matching algorithm for IdeaOverflow (discussed in Section 2.1) required users to manually choose keywords for the idea and simply searches for those keywords in the descriptions of other ideas already in the database.

Next we implemented two basic algorithms for matching ideas, based on theories I and IV in Section 2.2. To test them we created a command-line interface from from which the user can do simple things such as add ideas, add relationships, see suggestions of relationships, and make categories. (This is still under development and hence not yet integrated with the web interface.)

Figure 2.3-1. Command line interface for matching ideas

Linking ideas using commonsense knowledge

We used MIT ConceptNet 4 and Divisi2 to write one implementation of the method how_related_are_ideas(idea1, idea2), which works as follows.
- Extract a list of concepts from each idea.
- For each concept in the first list, find the most related idea in the second list using ConceptNet and Divisi.
- Average all the relatedness scores.

The “relatedness” metric is not simply a result of the physical similarity of an object to another, but is rather based on the paths connecting them in the entire OpenMind common sense knowledge graph. Thus, for example, while a cow is not physically similar to a bell, they are close in this metric since there is a “has a” relationship in the OpenMind graph between cow and bell.

Transitivity

After the user makes some connections between ideas, the method find_ideas_with_common_friends(idea1), takes the adjacency matrix of the relationships, normalizes the rows, and finds the other ideas (rows) which have the maximum dot product with the given idea, i.e., have the most common neighbors. Note how_related_are_ideas finds related ideas by commonsense reasoning, while find_ideas_with_common_friends finds related ideas using relations inputted by the user.

## 2.4 Results

We tested the program on a database of 29 ideas sourced from HackathonProjects.tk, a database of programming project ideas. Below is the result of finding related ideas to the following query: “app that suggests what you should cook, automatically orders ingredients or makes you a shopping list, and suggests who you should cook with.” The program suggests Emergency Pizza Button, GrabLunchWith, and Fridgey as the top related ideas (calculated using how_related_are_ideas).

Figure 2.4-1: Ideas most related to cooking app query

It also lists the most related concepts between the two ideas along with the relatedness score.

Figure 2.4-2. Most related concepts between cooking app query and GrabLunchWith app

The top 3 related ideas selected by the algorithm were the same top 3 ideas as selected by a human user in this instance. In general, preliminary qualitative testing reveals that the system nearly always automatically suggests the top 3 related matches in the top 10 suggestions.

## 2.5 Future work

In the future we will link the website with the idea matching algorithms. Based on our theories of how people link ideas, we would like to implement the following improvements to the idea linking algorithm.
- Perform idea linking on both the problem (gestalt) field and the solution field of each idea, and display for the user whether the connections between ideas are based on the common problems they are solving, or common solution techniques.
- Allow the user to make connections not just between ideas but also between ideas and categories--in effect, treating categories like ideas themselves. When a lot of ideas in a single category are highly related to a given idea, rather than show all of them, just show the category of the idea. This frees up the list of related ideas for ideas which are related in other ways.
- Use the hypernym framework in Conceptnet 5/Wordnet to trace words up a hierarchy. To compare ideas, trace individual concepts up to a middle layer of abstraction and compare the ideas at that level (for example, concepts “dog” and “cat” could be replaced by “pet”).
- Combine the commonsense framework with a story understanding engine such as Genesis.

There would also be value in creating a battery of standard tests researchers could run their idea relation algorithms against, to concretely measure their performance.

We also plan to create an explorable graph visualization of how ideas in the database connect. In particular, categories will be grouped together using the same color; when the user zooms out the nodes in the category can be replaced by a single node.

Figure 2.5-1. Mockup of clustered graph visualization of ideas

# 3 IdeaOverflow enables societal collaboration

## 3.1 Philosophical underpinnings: Gestalt theory

One way the human mind’s ideation process can be understood is through the framework of gestalt theory. Gestalt theory is a psychological paradigm that can be applied to help understand phenomena as seemingly disparate as human motivation, aesthetics, and ideation. Gestalt theory reveals why the process of ideation is not limited to a single mind, and moreover, gives us a method for projecting ideation into a shared space. Finally, knowledge of gestalt theory helps us understand why in building a system to process gestalts we are modeling a very fundamental process of human intelligence.

Literally, in German, gestalt means “form,” and refers in the abstract to the human desire to complete things that are aesthetically incomplete, or, in the parlance of gestalt psychology, to close open gestalts. As a basic example, in the Kanisza triangle illusion (Figure 3.1-1), the viewer perceives the presence of a bright white triangle where one is only outlined. When the brain sees elements that suggest a shape, it hallucinates the presence of a complete shape. Gestalt psychology explains this as a result of the brain’s desire to complete an uncompleted form, to close an open gestalt.

Figure 3.1-1. Kanisza triangle illusion

[But the real power of gestalt theory lies in applying the idea of closing open gestalts more abstractly. A more general way an open gestalt can be defined is as anything that tugs on a person’s attention. For instance, a feeling of hunger is an open gestalt: it draws your attention away from whatever you’re thinking about and towards your belly (starting a cascade of events to close the gestalt, respond to it, e.g., by obtaining food). Similarly, a desire to meet someone, an urge to write down an inspiration, a need to close a loose end in a story, and even a desire to complete an uncompleted chord progression in music can also be considered open gestalts: they sit in the back of your mind demanding a small piece of your attention until you finally respond to them.[1]](#ftnt1)

 What we draw upon in building IdeaOverflow is the fact that the human ideation process can be understood as the process of responding to open gestalts. When our brains assemble an idea that has the capacity to close an open gestalt, we remember it as worthwhile. Our brains continuously hold many open gestalts. Thus, we have tensions bending ideas into shape in our minds all the time. One way an idea can be good on many layers is when it has the capacity to close many open gestalts, integrating information and cleverly responding to manifold and subtle constraints. IdeaOverflow can be helpful in creating such ideas as the following case study shows.

##

## 3.2 Case study: How did “FoodMom” app idea develop?

As a case study, let us trace the pathways of open gestalts through which the app idea FoodMom, “app that suggests what you should cook, automatically orders ingredients or makes you a shopping list, and suggests who you should cook with,” was invented.
- First we are hungry.
- Thus we want to eat, and one common pathway of resolving this is cooking.
- Cooking requires first deciding what to cook, and then obtaining ingredients.

The first atomic challenge we encountered was the problem of deciding what to cook; thus we were inspired to make an app to solve it. Seeing that ordering ingredients is the next step after deciding what to cook, we expanded our app to also order the ingredients after deciding what to cook. Next we realized that cooking is a social activity, so we see that we can simultaneously satisfy users’ open gestalt of wanting to interact with other people. Thus FoodMom was born of the connection between these three open gestalts.

How could an idea-linking system have facilitated the invention of FoodMom? Suppose we only had the idea of making an app that helps us decide what to cook, and our ideation stopped there. Once we input the idea into the database, the idea relation engine would ideally traverse a knowledge graph such as ConceptNet in a fashion similar to the following:
- First, it would see that “deciding what to cook” is a subgoal of “cook.”
- It would see that “ordering ingredients” is another subgoal of “cook,” in fact, the next step after “deciding what to cook.” It would hence say our idea is related to ideas that relate to ordering ingredients, such as ActualFood, a company that gives same-day grocery delivery to refrigerated kiosks in users’ neighborhoods.
- It would see that “cooking” is one way to “socialize.” It would hence say that our idea is related to ideas that relate to “socializing.” For instance, FoodMom may be related to Instaquote, one feature of which is to match people who would like to meet each other based on the quotes they like.

From all these suggested relationships, it would have been clear to expand our app idea to also order ingredients and decide who to cook with, even though we did not make the connection between “cooking” and “social activity” in our own minds.

It is important to understand gestalt psychology as one of the underpinnings of the project because it helps us understand why IdeaOverflow has the potential to be a fundamental development: it facilitates the process of connecting, and thus more effectively closing, open gestalts, which, according to proponents of gestalt theory, is the fundamental human activity. Thus the system can be applied to facilitate ideation in virtually every creative endeavor. Moreover, realizing that IdeaOverflow is a gestalt-processing system, in conjunction with society of mind theory,  makes clear why it should have the capacity to naturally make ideation a collaborative process: even within an individual person’s mind, these theories posit, ideation is already a collaborative process between the agents in a person’s mind (which respectively voice each of the open gestalts a person currently has). Thus, with the right communication technology, it is not such a leap to see how the creative process can function smoothly across physically separate humans.

# Works Cited
Barlow, H. (1961) "Possible principles underlying the transformation of sensory messages" in Sensory Communication, MIT Press

[Hollan, James,  Edwin Hutchins, and David Kirsh. 2000. Distributed cognition: toward a new foundation for human-computer interaction research. ACM Trans. Comput.-Hum. Interact. 7, 2 (June 2000), 174-196. DOI=10.1145/353485.353487 http://doi.acm.org/10.1145/353485.353487](http://doi.acm.org/10.1145/353485.353487)

Hutter, M., Towards a Universal Theory of Artificial Intelligence based on Algorithmic Probability and Sequential Decisions, Proceedings of the 12th European Conference on Machine Learning (ECML-2001) 226-238, 2000.

Hutter M. Universal Algorithmic Intelligence: A mathematical top->down approach. Artificial General Intelligence, 2007, Springer, pages 227-290.

 Minsky, Marvin. 1986. The Society of Mind. Simon & Schuster, Inc., New York, NY

[Salomon, Gavriel (1997). Distributed cognitions: Psychological and educational considerations](http://books.google.com/books?id=m8Yna0cjxAgC). Cambridge University Press.

Gentner, Dedre, Keith James Holyoak, and Boicho N. Kokinov. The Analogical Mind:
Perspectives from Cognitive Science. Cambridge, MA: MIT, 2001. Print. 499.

[Winston, P. (2011). The Strong Story Hypothesis and the Directed Perception Hypothesis. Technical Report FS-11-01, Papers from the AAAI Fall Symposium, Menlo Park, CA (pp. 345-352). Retrieved from http://dspace.mit.edu/handle/1721.1/67693](http://dspace.mit.edu/handle/1721.1/67693)

# Appendix: Source Code
Attached is the core logic idea_mapper.py of the idea matching algorithm and the content of the database of 29 ideas, idea_db.txt.

idea_mapper.py
#!/usr/bin/env python#!/usr/bin/env python
# -*- coding: utf-8 -*-
importmath
fromd4dimport d4d
importsys
fromcscimport divisi2

classIdea:
def__init__(self,title="",text="",tags=""):
self.title=title
self.description=text
self.more=""
self.problem=""
self.solution=""
self.technology=""
self.tags=tags
Tags:, extract, concepts, from, idea, and, store, them
self.extract()
Tags:, print, "concepts:, ",self.concepts
self.related_ideas=[]
Tags:, maybe, add, an, idea, ID, number
self.populated=False
self.ID=0
defsetID(self, i):
self.ID=i
def__str__(self):
returnself.title+"\n Description:"+self.description+"\n Tags:"+str(self.tags)+"\n Related Ideas:"+self.print_related_ideas()
defextract(self):
self.concepts=extract_concepts(self.description)
defextend_related_ideas(self,li):
self.related_ideas.extend(li)
self.related_ideas.sort(lambda a,b:b[1]-a[1])
defprint_related_ideas(self):
                s=""
for (i,rel) inself.related_ideas:
                        s=s+str(i.ID)+" "+i.title+": "+i.description[0:50]+" "+str(rel)+"\n"
return s

defread_next_idea(f):
        i=Idea()
        prev_field=None
        cur_string=""
        s=f.readline()
if s=="\n":
returnNone
whileTrue:
if s=="\n":
Tags:, print, "updating, ",prev_field,", with, ",cur_string
globals().update([[prev_field,cur_string]])
break
                new_field=which_field(s)
Tags:, print, "New:",, new_field
Tags:, print, "String:",cur_string
if new_field!=None:
if prev_field!=None:
Tags:, print, "updating, ",prev_field,", with, ",cur_string
globals().update([[prev_field,cur_string]])
                        cur_string=s[len(new_field)+1:]
                        new_field=new_field[:-1].lower()
                        prev_field=new_field
else:
                        cur_string=cur_string+s
                s=f.readline()
Tags:, there, should, be, an, easier, way, to, do, this
        i.title=title[:-1]
        i.description=description
        i.more=more
        i.problem=problem
        i.solution=solution
        i.technology=technology
        i.tags=tags
return i

defwhich_field(s):
        fields=["TITLE:","DESCRIPTION:", "MORE:", "PROBLEM:", "SOLUTION:", "TECHNOLOGY:", "TAGS:"]
for f in fields:
if s[0:len(f)]==f:
return f
returnNone

classDatabase:
def__init__(self,db=None,mat_string=None):
self.d={}
self.ideas_list=[]
self.related_ideas_dict={}
self.f=None
self.read_from_file(db)
Tags:, create, a, sparse, matrix, from, ideas.
if mat_string==None:
self.idea_matrix=divisi2.SparseMatrix.square_from_named_entries([(0,0,0)])
else:
self.idea_matrix=divisi2.load(mat_string)
self.categories=None
defadd_cat(self,li,row_num=-1):
                l=len(li)
if l==0:
return
                v=[1for i in li]
if row_num==-1:
ifself.categories==None:
                                row_num=0
else:
                                row_num=self.categories.shape[0]+1
                rows=[row_num for i in li]
                mat=divisi2.SparseMatrix.from_named_lists(v,rows,li)
ifself.categories==None:
self.categories=mat
else:
self.categories=self.categories+mat
defread_from_file(self,db):
if db!=None:
                        i=1
self.f=open(db,'a+')
                        i=read_next_idea(self.f)
while i!=None:
self.add(i)
                                i.extract()
                                i=read_next_idea(self.f)
Tags:, i,j, are, indices, to, ideas
defconnect_ideas(self,i,j):
                mat=divisi2.SparseMatrix.square_from_named_entries([(1,i,j),(1,j,i)])
self.idea_matrix=self.idea_matrix+mat
deffind_ideas_with_common_friends(self,i,num_friends=5):
Tags:, normalize, each, row
try:
                        normalized=self.idea_matrix.squish().normalize_rows()
except:
return
Tags:, find, the, row
                row=normalized[i]
                a=normalized.dot(row)
Tags:, nbs=row.dot(normalized.transpose())
                maxV=0
                maxI=0
                b=sorted(a.entries(),reverse=True)                      
for i inxrange(min(5,len(b))):
                        idea=self[b[i][1]]#print the idea
print idea.ID, " ", idea.title, ", ", b[i][0]
defadd(self,i,add_to_file=False):
Tags:, related_ideas=self.get_related_ideas(i)
Tags:, i.extend_related_ideas(related_ideas)
self.d[i.title]=i
self.ideas_list.append(i.title)
                i.ID=len(self.ideas_list)-1
if add_to_file:
self.f.write("TITLE: "+i.title+"\nDESCRIPTION: "+i.description+\
"\nMORE: "+i.more+"\nPROBLEM: "+i.problem+"\nSOLUTION: "+\
"\nTECHNOLOGY: "+i.technology+"\nTAGS: "+i.tags+"\n\n")
defextend(self, li):
for i in li:
self.add(i)
defpopulate_related_ideas(self, i):
                li=self.get_related_ideas(self[i],False)
self[i].related_ideas=li
self[i].related_ideas.sort(lambda a,b:signum(b[1]-a[1]))
self[i].populated=True
defpopulate_all_related_ideas(self):
for i inself.d.values():
                        populate_related_ideas(i)
def__getitem__(self,i):
iftype(i)==str:
returnself.d[i]
Tags:, index, by, id, too?, Maybe, this, is, not, necessary.
eliftype(i)==int:
returnself.d[self.ideas_list[i]]
return
defhow_related_are_ideas(self,idea1,idea2):
return how_related_are_concept_lists(idea1.concepts, idea2.concepts)
Tags:, how, do, we, compute, this?
defget_related_ideas(self,qidea,allow_repeat=True):
Tags:, idea, already, has, extracted, concepts, stored
                relatedness = []
for i inself.d.values():
if (allow_repeat or i!=qidea):
                                relatedness.append((i, self.how_related_are_ideas(qidea,i)))
returnsorted(relatedness, reverse=True)
Tags:, list, truncated, to, top, 5
def__str__(self):
                s=""
for (i,title) inenumerate(self.ideas_list):
                        s=s+str(i)+" "+title+"\n   "+self[i].description+"\n"
return s
defprint_related_categories(self,i):
pass

defextract_concepts(idea):
        a=d4d.en_nl.extract_concepts(idea, check_conceptnet=True)
Tags:, print, "Extracting, from, ",idea
Tags:, print, "Concepts, extracted:, ",a
return a# max_words=2, check_conceptnet=True)

defsignum(a):
if a>0:
return1
if a<0:
return-1
return0
'''
calculates how related two concepts are
'''
defhow_related_are(concept1, concept2):
Tags:, print, concept1,, concept2
try:
return d4d.d4d.c4.how_related_are(concept1, concept2)
exceptKeyError: # key does not exist
Tags:, print, "key, error, ",concept1,", ",concept2
return0

'''
calculates how similar two concepts are
'''
defhow_similar_are(concept1, concept2):
Tags:, print, concept1,, concept2
try:
return d4d.d4d.c4.how_similar_are(concept1, concept2)
exceptKeyError: # key does not exist
Tags:, print, "key, error, ",concept1,", ",concept2
return0

defhow_related_are_concept_lists(concept_list1, concept_list2, metric_num=2):
        s="how_related_are_concept_lists"+str(metric_num)
returnglobals()[s](concept_list1, concept_list2)

Tags:, first, implementation:, take, top, 5, relationships
defhow_related_are_concept_lists1(concept_list1, concept_list2):
"""returns numerical relationship level 0 and up"""
        maxVs=[0,0,0,0,0]
        maxCs=[('',''),('',''),('',''),('',''),('','')]

for c1 in concept_list1:
for c2 in concept_list2:
                        r=how_related_are(c1, c2)
if r>maxVs[0]:
                                maxVs[0] = r
Tags:, maxVs.insert(0,r)
Tags:, maxCs.insert(0,(c1,c2))
Tags:, maxVs.pop()
Tags:, maxCs.pop()
                                maxVs.sort()

Tags:, print, maxCs
returnsum(maxVs)

Tags:, second, implementation:, take, top, relationships, with, each, concept, in, the, first, list,
Tags:, and, normalize
defhow_related_are_concept_lists2(concept_list1, concept_list2):
Tags:, print, "lists:, ",concept_list1,concept_list2
        maxVs=[]#0,0,0,0,0]
        maxCs=[]#('',''),('',''),('',''),('',''),('','')]
for c1 in concept_list1:
                maxV=0
                maxC=('','')
for c2 in concept_list2:
Tags:, print, (c1,c2)
                        r=how_related_are(c1, c2)
if r>maxV:
                                maxV = r
                                maxC=(c1,c2)
                maxVs.append(maxV)
                maxCs.append(maxC)
Tags:, print, maxCs
        total=sum(maxVs)/len(concept_list1)
        maxes=zip(maxVs,maxCs)
        maxes.sort(reverse=True)
for (r,(c1,c2)) in maxes:
print r," ",(c1,c2)
print"-------------"
print"Total: ",total
return total

Tags:, using, similarity
defhow_related_are_concept_lists3(concept_list1, concept_list2):
Tags:, print, "lists:, ",concept_list1,concept_list2
        maxVs=[]#0,0,0,0,0]
        maxCs=[]#('',''),('',''),('',''),('',''),('','')]
for c1 in concept_list1:
                maxV=0
                maxC=('','')
for c2 in concept_list2:
Tags:, print, (c1,c2)
                        r=how_similar_are(c1, c2)
if r>maxV:
                                maxV = r
                                maxC=(c1,c2)
                maxVs.append(maxV)
                maxCs.append(maxC)
Tags:, print, maxCs
        total=sum(maxVs)/len(concept_list1)
        maxes=zip(maxVs,maxCs)
        maxes.sort(reverse=True)
for (r,(c1,c2)) in maxes:
print r," ",(c1,c2)
print"-------------"
print"Total: ",total
return total

Tags:, using, hypernyms
defhow_related_are_concept_lists4(concept_list1, concept_list2):
Tags:, print, "lists:, ",concept_list1,concept_list2
        maxVs=[]#0,0,0,0,0]
        maxCs=[]#('',''),('',''),('',''),('',''),('','')]
for c1 in concept_list1:
                maxV=0
                maxC=('','')
for c2 in concept_list2:
Tags:, print, (c1,c2)
                        r=how_related_are(c1, c2)
if r>maxV:
                                maxV = r
                                maxC=(c1,c2)
                maxVs.append(maxV)
                maxCs.append(maxC)
Tags:, print, maxCs
        total=sum(maxVs)/len(concept_list1)
        maxes=zip(maxVs,maxCs)
        maxes.sort(reverse=True)
for (r,(c1,c2)) in maxes:
print r," ",(c1,c2)
print"-------------"
print"Total: ",total
return total

Tags:, third, implementation:, multiply, idea, vector, by, AA^T, by, idea, vector, 2,, where
Tags:, A, is, concepts*features, matrix.
##def how_related_are_concept_lists3(concept_list1, concept_list2):
##        #remove duplicates
##        concept_list1 = list(set(concept_list1))
##        concept_list2 = list(set(concept_list2))
##        len1=len(concept_list1)
##        len2=len(concept_list2)
##        if len1==0 or len2==0:
##                return 0
##        v1=[1/math.sqrt(len1) for i in concept_list1]
##        v2=[1/math.sqrt(len2) for i in concept_list2]
##        sv1=divisi2.SparseVector.from_lists(v1, concept_list1)
##        sv2=divisi2.SparseVector.from_lists(v2, concept_list2)
##        sv1.to_row().dot(
##        #
##        for (r,(c1,c2)) in maxes:
##                print r," ",(c1,c2)
##        print "-------------"
##        print "Total: ",total
##        return total

deflist_ideas(db):
print db
##def add_new(db):
##        title = raw_input("Enter idea title: ")
##        text = raw_input("Enter idea text: ")
##        print "Creating idea ",title
##        new_idea=Idea(title,text)
##        db.add(new_idea)
##        db.populate_related_ideas(len(db.ideas_list)-1)
##        print "Concepts in idea: ",str(new_idea.concepts)
##        print "Related ideas: ",new_idea.print_related_ideas()
defread_list(text):
        s=raw_input(text)
        l=s.split(" ")
return l
defadd_new(db):
        title =raw_input("Enter idea title: ")
        text =raw_input("Enter idea text: ")
        new_idea=Idea(title,text)
        db.add(new_idea,True)
        idea_id=len(db.ideas_list)-1
        db.populate_related_ideas(idea_id)
Tags:, print, "Concepts, in, idea:, ",str(new_idea.concepts)
print"Related ideas: ",new_idea.print_related_ideas()
whileTrue:
                l=read_list("Make relations with: ")
if l==[]:
break
for i in l:
                        db.connect_ideas(idea_id,int(i))
print"Related idea suggestions:"
                db.find_ideas_with_common_friends(idea_id)
defconnect(db):
        idea_id =int(raw_input("Idea 1 ID: "))
print"Related ideas: ",new_idea.print_related_ideas()
whileTrue:
                l=read_list("Make relations with: ")
if l==[]:
break
for i in l:
                        db.connect_ideas(idea_id,int(i))
print"Related idea suggestions:"
                db.find_ideas_with_common_friends(idea_id)
        id2 =int(raw_input("Idea 2 ID: "))
        db.connect_ideas(id1,id2)
deffind_related_idea(db):
        s=raw_input()
if s=="":
pass
else:
                i=int(s)
if db[i].populated==False:
                        db.populate_related_ideas(i)
print"Related ideas (commonsense): "
print db[i].print_related_ideas()
print"Related ideas (common relations): "
                db.find_ideas_with_common_friends(s)
Tags:, def, find_friend_idea(db):
#        s=int(raw_input("Idea ID:"))
#        db.find_ideas_with_common_friends(s)
defadd_category(db):
        l=read_list("ID's of ideas in category: ")
        db.add_cat(l)
defprint_category(db):
print db.categories
        s=raw_input("Category ID: ")
if s=="":
return
        l=read_list("ID's of ideas in category: ")
        db.add_cat(l,int(s))
deffind_related_category(db):
        s=raw_input()
if s=="":
pass
else:
                i=int(s)
if db[i].populated==False:
                        db.populate_related_ideas(i)
print"Related categories (commonsense): "
print db.print_related_categories(i)
defsave(db):
        divisi2.save(db.idea_matrix,"idea_mat.pickle")
defload(db):
        db.idea_matrix=divisi2.load("idea_mat.pickle")
defdisplay_reln(db):
print db.idea_matrix
defquit_program(db):
        sys.exit(0)

logic={0:"List ideas ",1:"Add new ",2: "Establish connection",\
3:"Find related ideas",\
# 4:"Find related ideas using mutual connections",\
4:"Add category", 5:"View and modify categories", 6: "Find related categories",\
Tags:, eventually, categories, should, be, treated, more, like, ideas
7: "Save", 8:"Load",\
9:"Display relationships",10:"Quit"}
logic2={0:list_ideas, 1:add_new, 2:connect,\
3:find_related_idea,\
#4:find_friend_idea,\
4:add_category, 5:print_category, 6:find_related_category,\
7:save, 8:load,9:display_reln,10:quit_program}
if __name__ =='__main__':
print'START\n'
##        i1=Idea("Pitch-based scrolling", "e.g. when you sing middle C, the document jumps to 50% mark. natural tool for voice recognition users/RSI/paralyzed patients")
##        i2=Idea("EEG-based Slumping Detector", "What if you could make an app for Google Glasses or similar that follows a person's eyes and then and tracks where they are focusing. This way, you could  compare how different people focus differently, and analyze what that does to their lives. I also imagine that you could you could put on glasses yourself (or watch a screen), and then see the world through another person's eyes. ~jcole@mit.edu")
##        i3=Idea("InstaBoxSite:", "platform to build: generalized, easy to modify \"suggestion box\" framework anyone can use to quickly buildp a website off that mold.  All of following sites and countless more are based on fundamentally the same idea of a \"comments box: isawyou stackoverflow forums reddit fml formspring ideaoverflow.tk / hackathonprojects.tk suggestion box/politicalprogressbar ifiwereanmitstudent.tk tumblr twitter facebook wall. In parallel, I am able to protoype many of the websites I build these days with what is basically a google doc. Why not build a google doc with slightly more functionality that truly allows me to prototype these tools? Check out http://mitdocs.tk/ to see the potential of this. Relatedly, way for people to make a homepage as easily as they can make a google doc -- consider http://adamchu.tk/, and http://minimalisthomepages.tk/  ~jcole@mit.edu")
        db=Database("idea_db.txt")
##        db.extend([i1,i2,i3])
##        print getRelatedIdeas(Idea('eeg scrolling','eeg scrolling'))
whileTrue:
for k in logic:
print k," ",logic[k]
                a=int(raw_input())
                logic2[a](db)

##                #warning: don't create duplicates
##                title = raw_input("Enter idea title: ")
##                if title=="":
##                        sys.exit(0)
##                text = raw_input("Enter idea text: ")
##                print "Creating idea ",title
##                new_idea=Idea(title,text)
##                db.add(new_idea)
##                db.populate_related_ideas(len(db.ideas_list)-1)
##                print "Concepts in idea: ",str(new_idea.concepts)
##                print "Related ideas: ",new_idea.print_related_ideas()

idea_db.txt
TITLE: Workflow sharing
DESCRIPTION: Take the workflows of top students and make or sell complete sets of customized materials to help other people adopt the workflows of the super productive people.
MORE: start up idea is to take the workflows of top students and make/sell complete sets of customize materials to help other people adopt the workflows of the super productive people.I think that that's half the battle, getting into the right life-rhythm. I bet for each stereotype of person, you can find some sort of optimize workflow and then you go and get the workflow kit for the type of person you are like are you like riley or (racks brains) my friend jenny or like cj whose system do you use well fine the person you learn like you could even make "learn like riley" or “learn like a thiel fellow” or “learn like a harvard student” “or _insert child prodigy here_” Example workflow “take a normal sheet of paper fold it hamburger style but then instead of folding it all the way to symmetry, give a quarter inch gap between the two folds then with the fold pointing to the right, fold it top-to-bottom 3 times unfold then write terms on outer flap, definitions on inner flap fold over, repeat IT'S HAPPY. I've done like 264 defines in 3 hours but actually a lot of perceived inefficiency or  failure /does/ come from shitty workflows once I have a system set up, the stuff practically teaches itself i'm just starting to hack school coursenotes: ocw formatting: latex killer ppts: magic markers THE LIST GOES ON.” In parallel, as college students, we’re  SITTING ON GOLD.(e.g.  my friends coursenotes/annotated copy of Poems Poets Poetry is a GOLDMINE. like she should just republish the darn anthology with her notes. http://www.scotthyoung.com/blog/ makes his business off of this i want the workflow of someone super geniusly good - Jacob (and Riley)
PROBLEM: People aren’t productive.
SOLUTION: Share workflows of productive people.
TECHNOLOGY:
TAGS: ~Jacob

TITLE: MedTime
DESCRIPTION: Track when people actually take their meds
MORE: what if you used an app to track when people actually /do/ take their meds
this is absolutely what we should be thinking about
there exist a number of drugs for which the main and important factor is the minimum blood level concentration is the important part
among these are birth control, seizure meds, beta-blockers and a whole bunch of other things
and you have to take them at the same time every day because you need to maintain minimum effective concentration
but, excepting beta-blockers, having a concentration in excess, up to about 3x the normal does, is not something that will hurt you
so, what would be cooler than reminding you to take your meds when you tend to sit down and eat dinner
is an app that analyzes when you actually do take your meds, and then suggests custom dosages based on your schedule
custom blister packs are actually not that hard, it's something that's done a lot for people who are on oral chemo and want to take more on the weekends because they have to work during the week
it's not something that's anywhere outside of the realm of physicians to prescribe, in fact, its actually in their best interest
PROBLEM: People don’t take their meds on schedule.
SOLUTION: Track when people actually take their meds, and remind them.
TECHNOLOGY:
TAGS: ~Riley

TITLE: Pitch-based scrolling
DESCRIPTION: Use voice to scroll.
MORE: Pitch-based scrolling - e.g. when you sing middle C, the document jumps to 50% mark. natural tool for voice recognition users/RSI/paralyzed patients
PROBLEM: People who are paralyzed can’t scroll.
SOLUTION: Use pitch to scroll.
TECHNOLOGY:
TAGS: ~Jacob

TITLE: EEG-based Slumping Detector
DESCRIPTION: Monitor posture and help correct it.
MORE: detect the pattern of brain activity that correlates with slumping / program that alerts me as is my posture begins to deteriorate so that I could correct it.. Could also just tells you to go to sleep. Helps people recover more quickly from RSI/carpal tunnel. Has interesting neuro/psych implications if it works as well. Would use Emotiv headset
PROBLEM: Slumping, bad posture.
SOLUTION: Monitor posture and help correct it.
TECHNOLOGY: EEG
TAGS: ~Jacob

TITLE: WorldThroughYourEyes
DESCRIPTION: Track where a person’s eyes are focusing, and analyze the effects on their lives.
MORE: What if you could make an app for Google Glasses or similar that follows a person's eyes and then and tracks where they are focusing. This way, you could  compare how different people focus differently, and analyze what that does to their lives. I also imagine that you could you could put on glasses yourself (or watch a screen), and then see the world through another person's eyes.
PROBLEM: People want to see the world differently.
SOLUTION: Track where a person’s eyes are focusing.
TECHNOLOGY: Google Glasses
TAGS: ~Jacob

TITLE: InstaBoxSite
DESCRIPTION: Build an easy to modify "suggestion box" framework anyone can use to quickly build a website off that mold.
MORE: platform to build: generalized, easy to modify "suggestion box" framework anyone can use to quickly build a website off that mold.  All of following sites and countless more are based on fundamentally the same idea of a “comments box: isawyou stackoverflow forums reddit fml formspring ideaoverflow.tk / hackathonprojects.tk suggestion box/politicalprogressbar ifiwereanmitstudent.tk tumblr twitter facebook wall
In parallel, I am able to protoype many of the websites I build these days with what is basically a google doc. Why not build a google doc with slightly more functionality that truly allows me to prototype these tools? Check out http://mitdocs.tk/ to see the potential of this. Relatedly, way for people to make a homepage as easily as they can make a google doc -- consider http://adamchu.tk/, and http://minimalisthomepages.tk/
PROBLEM: Many websites use the same kind of suggestion box.
SOLUTION: Make a framework for suggestion boxes.
TECHNOLOGY:
TAGS: ~Jacob

TITLE: virtual reality game with 3d-goggles in swimming pool.
DESCRIPTION: virtual reality game with 3d-goggles in swimming pool or indoor skydiving arena
MORE: virtual reality game with 3d-goggles in swimming pool. Or indoor skydiving arena that projects a zooming in Google Earth onto the floor below. Would be like <http://www.youtube.com/watch?v=gHo2eEVSqao> except with actual indoor skydiving than. Since while you're at terminal velocity you experience no toleration, this would be indistinguishable from actual skydiving (sans the initial drop), especially if you did this with virtual reality goggles. ~jcole@mit.edu
PROBLEM:
SOLUTION:
TECHNOLOGY: 3-D goggles
TAGS: ~Jacob

TITLE: Index card sharing
DESCRIPTION: Organize and share your thoughts by writing them concisely and linking them together.
MORE: A good way to organize your thoughts is to write them down concisely. An index card seems like a good length for a unit of thought: longer than a quote or decontextualized summary, shorter than a story or lesson. Index cards seem a good way to transmit thoughts: it is easy to learn information presented in bite-sized chunks, each centered around some principle you can easily remember. The title of the card can act as a "slogan" for the principle.
I am inspired by Trefethen's Index Cards: one mathematician wrote down his thoughts on science, education, politics, intelligence, etc. on ~350 index cards over a period of 40 years and published it as a book. (http://books.google.com/books/about/Trefethen_s_Index_Cards.html?id=hJT0tgAACAAJ)
Minsky's Society of Mind also strikes me as written in a similar way: while a page is more than an index card, the fact that each section is no more than a page has a focusing effect on the reader.
There are two parts to this project: allowing the user to create a system of cards, and then facilitating sharing.
Each index card has limited space but allows multimedia (for instance, putting in a simple picture/diagram as a symbol). You can hashtag index cards, search for others' cards on similar topics, rate cards, provide links, and make "connections" between different cards (and possibly specify the kind of connection, for instance hierarchical), much like a semantic net. This gives a way to visualize someone's thoughts (and almost "surf" their thoughts, in a way). I might have some good ideas which I write as a linear sequence of blog posts---but if I write them as index cards instead, this would force me to crystallize my ideas more, and allow them to be connected in a nonlinear fashion. Some possible uses: A card could be a quote, and then a anecdote around it. I could make one index card for every book I read, for instance---then anytime the book comes up in conversation I could pull up my index card on the phone and know exactly the thoughts I have about it, and be able to talk about it. (In fact, if I write up cards on a variety of topics, they could almost be a cheat sheet for conversation. If you had a repertoire of cards related to topics important to you, then you needn't grope for words, for instance, if someone asks about an aspect of your work. In fact, maybe they could check out your cards first, and the conversation could immediately proceed to something new!) I could use it for academics: a card could be a Theorem or Principle X, and contain the information I would need if, say, I had to give a talk on it on short notice.
PROBLEM: People’s thoughts are messy.
SOLUTION: Write them down on virtual index cards and organize them.
TECHNOLOGY:
TAGS: ~Holden, #organization

TITLE: Thoughtstream tool
DESCRIPTION: Make a central platform for thoughtstreaming.
MORE: Make a central platform that integrates status messages, facebook posts blog posts, favorite quotes, and liked songs -- in other words, a platform for thoughtstreaming. Relates to many earlier ideas ~jcole@mit.edu [I was thinking about this. At the end of the day I want to look at all my writing activity (fb, reddit, chat), and choose to (or automatically) add things I’ve written into my thought database. That way I can tag thoughts as I write, and not have to go back and search for them, or copy/paste in the moment ~ cj@cortexel.us ]
PROBLEM: People have ideas that they don’t record.
SOLUTION: Make a central platform for thoughtstreaming.
TECHNOLOGY:
TAGS: ~Jacob

TITLE: Flow Me
DESCRIPTION: Suggest rhymes and alliterations as you type.
MORE: Flow Me – Tool for making freestyling/rhyme/poetry unfairly easy. Suggests rhymes and alliterations as you type. Goal: to empower those with good messages and no writing skills. ~cj@cortexel.us #poetry #nlp #creativity #writing (Carl: check out http://tranquillpoet.com/ for inspiration!   Thank you!! That is awesome! This is a really elegant incarnation of the idea! Already getting a bunch of new ideas. Here are the beginnings of mine: http://cortexel.us/flow )
PROBLEM: People writing poems can’t think of rhymes.
SOLUTION: Suggest rhymes and alliterations as you type.
TECHNOLOGY:
TAGS: ~CJ

TITLE: DeviceSymphony
DESCRIPTION: a mobile or Web app that plays the same note you are singing
MORE: mobile app/Web app that plays the same note you are singing, or plays harmonics to the note you’re playing. This way, you could put all your mobile devices out on a table and sing and be accompanied by a whole orchestra!
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS: ~Jacob

TITLE: Fridgey
DESCRIPTION: Gives recipes based on what you have in your fridge.
MORE:  Scavenger Recipe App (aka Fridgey!) -- Enter what ingredients are present in your refrigerator, and it looks up possible recipes that include the ingredients entered, ranked by ratings and difficulty to make, for those days where you have a bunch of stuff in the fridge, but nothing to eat. This app can also log and track what ingredients you have available, so you do not have to enter your fridge inventory every time. A broke college student’s oasis. ~carlton.stafford@gmail.com  #<->FoodMom
Comments:
*Cool! They are definitely similar, but not the same, for one automatically orders ingredients you do not have, and the other shows you what you can make with what you do have. Combine them possibly?
*Question: Would ‘method of preparation’ be a worthy sub-category for the application? In other words, "Recipes that require baking", "Recipes to be prepared on a skillet." Or.. even better, “select the appliances/cooking materials accessible to you” (Can you suggest a less wordy way of saying this?) I am envisioning this in the form of a checklist. - acousticcole@gmail.com
*A checklist, or perhaps a filter interface, where you check appliances available, and it filters out options that would not work. That may be a little easier. carlton.stafford@gmail.com
http://www.instantfundas.com/2010/08/15-websites-to-find-recipes-by.html <- it exists.
PROBLEM: You have a bunch of stuff in the fridge, but nothing to eat.
SOLUTION: Gives recipes based on what you have in your fridge.
TECHNOLOGY:
TAGS: ~Carlton

TITLE: Build eyetracking heatmap from laptop webcam
DESCRIPTION: Build eyetracking heatmap from laptop webcam to evaluate how you read websites.
MORE: Build eyetracking heatmap from laptop webcam -- useful for evaluating how you read different websites, self-tracking/optimizing, and evaluating websites you build. You could make a script that lets you compare different people’s reading styles and evaluate the eye movement patterns of master readers. Also for online chess you could track eye movement patterns of novices vs masters as part of the coaching -- this has been studied extensively. #cv ~hbedri@mit.edu  ~jcole@mit.edu
PROBLEM:
SOLUTION:
TECHNOLOGY: eyetracking, webcam
TAGS: ~hbedri, ~Jacob

TITLE: Google docs optimized for instant web publishing
DESCRIPTION: Google docs optimized for instant web publishing
MORE: Google docs optimized for instant web publishing #idea #good #lowhangingfruit ~jcole@mit.edu. An important facet is to combine with easy-to-remember domains like .tk. I was reinspired in the direction of this project after a resounding success building a collaborative doc, http://6034bonus.tk, for my AI class final notes yesterday; Google docs are great because they're such a fast way to prototype so many web ideas. See also http://mitdocs.tk/ and derivatives. I wish they just created pages that were a bit more... web 2.0-y that were a pleasure to view as well as edit. Also, I wish you could do align left and align right on the right and left-hand sides of the same line. This is, I feel, the basis for an entirely new creative outlet. Is anybody who is good with node.js want to experiment with sharejs maybe? <http://sharejs.org/>? Note: doing so would be the stepping stone into a whole, tightly connected bunch of projects to which I've given much thought and with which I am completely willing to help.  #<->Way to track traffic on Google Docs/quick way to a
ssign a google doc to a .tk domain
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS: ~Jacob

TITLE: Google doc tools
DESCRIPTION: Track traffic on Google Docs and quickly assign a google doc to a .tk domain.
MORE: Way to track traffic on Google Docs/quick way to assign a google doc to a .tk domain #<->Google docs optimized for instant web publishing ~jcole@mit.edu
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS: ~Jacob

TITLE: Emergency Pizza Button app
DESCRIPTION: One-click pizza ordering via a big red button
MORE: Emergency Pizza Button app -- One click pizza ordering via a big red button, modeled after the MIT east campus emergency pizza button.  Relatedly, I want to make “Push a button, get a cookie” app for Insomnia Cookies. ~jcole@mit.edu #active
PROBLEM: Ordering pizza takes time.
SOLUTION: One-click pizza ordering
TECHNOLOGY:
TAGS: ~Jacob

TITLE: PhotoQuote
DESCRIPTION: Photograph a quote, find the quote online, and record it.
MORE: PhotoQuote -- app that lets you photograph a quote in a book, then searches online to find the boundaries of the quote you're probably looking to note down, and adds the quote to your notebook. I find myself photographing quotes all the time. This is a big idea, and knowing the thread of quotes a person is interested in is a very powerful, and truly relevant advertising dataset. #relates to “site that autocompletes quotes” #intentiondb
PROBLEM:
SOLUTION:
TECHNOLOGY: OCR
TAGS: ~Jacob

TITLE: Instaquote
DESCRIPTION: Autocomplete quotes, create a database of quotes you’re interested in.
MORE: Instaquote -- site that autocompletes quotes like instadefine.com  and it basically ends up letting you create a database  of quotes you're interested in
and this is deep because quotes are your thoughts stated more clearly than you can state them yourself and if you make a db of all the quotes people think of  you get a huge window into their lives  it #relates to the power of status message logging. example:  is  send myself  email  of quotes I like  for instance  "and it scared me, having a wrong thought, because it meant my mind wasn't working properly"  from the curious incident of the dog in the night-time  i just was rereading today and i realized that was brilliant  because it relates to a concept  of avidya  in eastern philosophy the idea that there are some thoughts that we have that aren't true, but instead  things that shouldn't bother us bother us  and when we think carefully and relax we can learn to only be bothered by the right things  (relatedly, there's a lot to be done with etymology) #intentiondb ~jcole@mit.edu
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS: ~Jacob

TITLE: FoodMom
DESCRIPTION: App that tells you what to cook, automatically orders ingredients (or makes you a shopping list), and suggests who you should cook with.
MORE: FoodMom -- App that tells you what to cook and automatically orders ingredients (or makes you a shopping list). Also suggest who you should cook with using the following meeting people strategy:” ~Jacob   +1 ~csvoss@mit.edu ~jcole@mit.edu #6.470 Meet people who have similar interests by matching people to each other who have mentioned titles to the same Wikipedia articles in their gmail chats, or used the same quotes. (Or it could look at your playlist history and match by music taste! (real “musicmatch”)). Cooking/eating is one of the few anchors to physical world in an era of increasing digital distraction, and we should use it to resurrect classic face to face socialization. Ideas. Starts with http://foodlists.tk/ #primer #lifecoach
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS: ~Jacob

TITLE: Call for Fall
DESCRIPTION: Detect when an old person has fallen, and makes an emergency call.
MORE: -app that uses accelerometer data to detect when you (an old person) have fallen. If you don’t touch a button in 1 min cancelling emergency call, it calls your relatives who check if you’re okay, and broadcasts your gps location. ~jcole likes this one -- email me if you want to work on it! #<-> ginger.io #lowhanging #humandatamining #machinelearning  ~jcole@mit.edu
PROBLEM: Old people fall.
SOLUTION: Detect when an old person has fallen, and makes an emergency call.
TECHNOLOGY: accelerometer
TAGS:

TITLE: ThisIsHowYouSoundRightNow
DESCRIPTION: Determines your alertness level by using machine learning on keystrokes
MORE: ThisIsHowYouSoundRightNow (or ThisIsHowYouLookRightNow) -- app that determines if you’re in “hack mode” or “lazy mode” (alertness level) by using machine learning on keystrokes. Make hack-o-meter. Also make it so that it shows a picture of you from webcam when you’re drowsy so you look at yourself and see you need to go to sleep #humandatamining #machinelearning ~jcole@mit.edu
PROBLEM: We can’t tell if we’re being productive.
SOLUTION: Determines your alertness level by using machine learning on keystrokes
TECHNOLOGY: Machine learning
TAGS: ~Jacob

TITLE: News Timelines
DESCRIPTION: Organize related news articles into timelines so you can see the meaning of each article
MORE: Organize related news articles into timelines so you can see the meaning of each article, and maybe join in! #intentiondb ~jcole@mit.edu
PROBLEM: It’s hard to follow news.
SOLUTION: Organize related news articles into timelines
TECHNOLOGY:
TAGS: ~Jacob

TITLE: CuriosityThread
DESCRIPTION: Show the chain of questions or interests a person asked or followed to gain the knowledge and passion they have.
MORE: CuriosityThread -- Site that shows the chain of questions/interests a person asked/followed to gain the knowledge/passion they have. Perhaps to partially populate this site, Wikipedia could track threads of browsing, and scrolling. Subsequently, tutorials (even a textbook!) customized to the curiosity profiles of different people could be made of it? Relatedly, creating a web database of the series of questions bright students ask could be extremely powerful. I would love, for instance, to have documentation of the series of questions one of my friends asked over the course of his life to ultimately gain the knowledge to get gold at the International Chemistry Olympiad. #edu #<->admitsphere #<->whyisitawesome. #active, see http://curiositythread.tk/ or http://whyisitawesome.wikispaces.com/ ~jcole@mit.edu
PROBLEM: Follow someone’s learning process.
SOLUTION: Record and show the chain of questions or interests a person asked or followed to gain the knowledge and passion they have.
TECHNOLOGY:
TAGS: ~Jacob

TITLE: IdeaOverflow
DESCRIPTION: Allow people to share good ideas that they don't necessarily have time to implement themselves online.
MORE: IdeaOverflow -- A place people can share good ideas that they don't necessarily have time to implement themselves online. I want to make a map, a connected graph, of all of peoples' ideas (and implemented engineering projects) that shows the relationship of these projects to one another. At the borders of this graph would lie the ideas that are yet to be implemented -- investigating them more deeply would be analogous to exploring undiscovered terrain on a map. This tool would help people to come up with awesome ideas for hackathons, class projects, startups, and fun, and it also allow people to see  the trends/relationships in exciting ideas that are surging at a given point in time. Most of all, it's inspiring to think that through this system, you could bring vitality to the education industry by reducing every class project to, at worst, implementing an idea that someone, somewhere would be really excited to build if they had the time to. #intentiondb ~jcole@mit.edu
PROBLEM: Ideas are not equally distributed in people.
SOLUTION: Allow people to share good ideas that they don't necessarily have time to implement themselves.
TECHNOLOGY:
TAGS: ~Jacob

TITLE: PoliticalProgressBar
DESCRIPTION: A simple GUI that voters can use to quickly see what government is trying to accomplish and how far it has gotten towards achieving its goals. It would take the form of a progress bar.
MORE: PoliticalProgressBar -- I want to create a simple graphical interface that voters can use to quickly see what government is trying to accomplish and how far it has gotten towards achieving its goals -- it would perhaps take the form of a progress bar.
More generally, the deeper significance of many news items can be revealed on interface such as this -- if a certain piece of sustainable energy legislation passes, how much closer has it gotten us as a nation and planet to actually being energy sustainable for the forseeable future? This system would graph that kind of information on timeline/progress bar, the position (% completion) of which could be determined roughly by a consensus of scholarly opinions.
Above all, I want to make a database of thoughtful people and politicians' dreams -- their collective positive visions for how the world should be -- then find the most rational way to make those dreams real (e.g. elect the senators that have the competence, vision, and concrete plans necessary. Are trickle down economics or Obamanomics better for creating a vibrant economy that allows people to live the American dream? I don't know. Let's look at the research and find out, and take the most rational action.) #intentiondb ~jcole@mit.edu
PROBLEM: Voters can’t gauge how successful government is.
SOLUTION: A simple GUI that voters can use to quickly see what government is trying to accomplish and how far it has gotten towards achieving its goals.
TECHNOLOGY:
TAGS: ~Jacob

TITLE: EveryDayOfYourLife
DESCRIPTION: Ask a user to answer daily questions for self-reflection and share answers
MORE:
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS:

TITLE: Minimalist homepages
DESCRIPTION: Quick workflow to make minimalist homepage for yourself using Google docs and tk domains
MORE:
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS:

TITLE: GrabLunchWith app
DESCRIPTION: Suggests where you should have lunch, and recommends friends to go to the same place so they meet.
MORE:
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS:

TITLE: Academic conversations tool
DESCRIPTION: matches people that have mentioned titles to the same Wikipedia articles in their chats, or quotes
MORE:
PROBLEM:
SOLUTION:
TECHNOLOGY:
TAGS:

4
[[1]](#ftnt_ref1)Even the classic tenet in playwriting, Chekhov’s Gun--the idea that an author should not put a gun on the wall in the set of a play unless it will go off later--can be explained in terms of gestalt theory. The presence of a gun opens a gestalt. If it does not go off, the audience wastes their attention speculating about it for the entire play, and they feel disappointed. On the other hand, if at long last, the gun does go off, their attention was worthwhile.