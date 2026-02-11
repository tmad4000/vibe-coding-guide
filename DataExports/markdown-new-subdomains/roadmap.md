[[#connectordoc #ideaflowpan        systematicawesome.jacobcole.net](http://systematicawesome.jacobcole.net/)> roadmap.jacobcole.net](http://roadmap.jacobcole.net)
[started by jacob@ideaflow.io](mailto:jacob@ideaflow.io)
Ideaflow Roadmap
[[[[[[See also: Current](https://docs.google.com/document/d/1-SzJqsDZbMY3N_7dDMty28FUc4WA5mPwhuq6xO8_tmE/edit) •  Path to Product-Market Fit (formerly: Path to Series A) V1.4 (May 18 2020)](https://docs.google.com/document/d/1nnP-45KiW2CmncF6Yn1HvIvQcBHGh63SzKkC1blmknc/edit#heading=h.xx6ibmlpkgj8)  • businessroadmap.jacobcole.net](https://businessroadmap.jacobcole.net/) • Productfeedback.jacobcole.net](http://productfeedback.jacobcole.net) • ideaflowproject.jacobcole.net](http://ideaflowproject.jacobcole.net/) •User Profiles and Feedback Doc](https://docs.google.com/document/d/1MXvmAOcMZg0Qo_w6SvcdxVina2LkZcgU19lU6HtTOok/edit)

# 2022-09-30 Current Roadmap (Sprint Planning)

### #goal 100 active users whose value from ideaflow is quick capture + 10 power users.

### Sprint Planning Outline From Jacob
Key insight: Just having the basic ThoughtStream and search that works stably and quickly and offline is a huge value prop and awesome!

Q4 2022
- Offline (polish) #category
- Fast Load Time

- [[[linear](https://linear.app/ideaflow/issue/ENT-1500/investigate-load-time-on-jacobs-instance)] Sep 30 2022: Current load time for jacob on develop (39k notes) is 9 sec. No need to fixate on supporting >10k notes for now, if it’s difficult, but ideal: basic actions all under 100ms to interactibility a la Superhuman](https://crm.org/news/superhuman-email-a-whole-new-category-of-speed#:~:text=Buchheit%20states%20every%20interaction%20should,the%20program%20to%20performing%20searches). We can fudge this in lots of ways, e.g. allow typing new note or search without loading all notes. We also don’t have to fully achieve this in all interactions now. Goal #explainingIdeaflow: “become the superhuman of Tools for Thought”
- Make search field interactable even before main note is loaded #10-24

- Make “No notes containing "asdffdfsgdsg" found. Why not create one?” have the search text as actual body of the note when you create. Shortcut, perhaps cmd+enter to create

- While notes are loading, have a first, blank note that allows user to start typing. Spinner could occur below. Could even be just a textarea for MVP. Only activates if user has >10k notes perhaps? a quick capture popup could alternatively solve this #tweak

- Condensed View

- [Make condensed view bullets](https://linear.app/ideaflow/issue/ENT-1501/condense-bullets) considered separate entries
- Make condensed view entries not have “show more” if there’s nothing more to see
- Play with style/bg color on condensed view
- “Distributive property” with hashtags alone on a line — should apply to all following paragraphs

- [Reverse relations to](https://linear.app/ideaflow/issue/ENT-1245/expand-back-references-in-line) show up in inline expansion

- Bug fixes

- [[linear](https://linear.app/ideaflow/issue/ENT-1432/safari-ios-and-macos-doesnt-accept-login-cookies-if-auth0-website-is)] fix login issue
- [??[github](https://ideaflowteam.slack.com/archives/C028U0USYCC/p1664548171466759?thread_ts=1664525835.544269&channel=C028U0USYCC&message_ts=1664548171.466759)] Sep 30 2022: bug in develop with + creation, see #user-feedback
- [[[[[linear](https://linear.app/ideaflow/issue/ENT-1476/remove-turn-off-airplane-mode-to-access-data-warning-on-mobile-if-on)] Remove “turn off airplane mode to access data” Warning when offline [a]](#cmnt1)[b]](#cmnt2)[c]](#cmnt3) #postponed? #ttt
- [[??[slack] #bug basic search isn’t working on develop for me fyi](https://ideaflowteam.slack.com/archives/C028U0USYCC/p1664528757947959)https://share.getcloudapp.com/p9uQXdXG](https://share.getcloudapp.com/p9uQXdXG) merged, working in develop
- [[slack] #bug #minor — if there is a current filter condition including the hashtag you’re typing, hashtag autocomplete doesn’t work #ux](https://ideaflowteam.slack.com/archives/C028U0USYCC/p1663123769883849) 1503 #10-24
- [[[[[[linear](https://linear.app/ideaflow/issue/ENT-1503/cannot-accept-suggestions-while-searching-on-hashtags)] [slack] #bug For some reason a hashtag that should exist isn’t](https://ideaflowteam.slack.com/archives/C028U0USYCC/p1663870788672829)showing](https://ideaflowteam.slack.com/archives/C028U0USYCC/p1663870788672829)[d]](#cmnt4) up in the auto complete here](https://ideaflowteam.slack.com/archives/C028U0USYCC/p1663870788672829)

- [[[linear 1](https://linear.app/ideaflow/issue/ENT-1472/sw-should-ask-all-cli-for-the-auth-tokens)] [linear 2](https://linear.app/ideaflow/issue/ENT-1473/investigate-syncing-less-often-at-key-moments)] Sync doesn’t always happen automatically when i open my laptop after having used my ipad. Needs refresh
-
- [references disappear #bug https://share.getcloudapp.com/kpuW4w7R](https://share.getcloudapp.com/kpuW4w7R) #tttt #10-24
- [“Publish is broken :////” #user-feedback](https://ideaflowteam.slack.com/archives/C028U0USYCC) #bug ~anna brewer #ttt #10-24

- UX tweaks

- [[[[[[having](https://linear.app/ideaflow/issue/ENT-1504/take-into-account-prefix-match-into-sorting-autocomplete-suggestions)exact](https://linear.app/ideaflow/issue/ENT-1504/take-into-account-prefix-match-into-sorting-autocomplete-suggestions)[e]](#cmnt5)[f]](#cmnt6)[g]](#cmnt7) or prefix](https://linear.app/ideaflow/issue/ENT-1504/take-into-account-prefix-match-into-sorting-autocomplete-suggestions) match occur at top of + relation list
- Polish shortcuts, e.g. for inline expansion etc. E.g. cmd down

- [[shortcut  to Pivot](https://linear.app/ideaflow/issue/ENT-1505/shortcut-to-pivot-around-left-most-hashtag)around hashtag](https://linear.app/ideaflow/issue/ENT-1477/req-have-cmd-enter-pivot-around-hashtag-currently-under-the-cursor) cursor is currently on? #10-24
- Recreate cmd + b for bold
- [[[linear](https://linear.app/ideaflow/issue/ENT-1441/pressing-escape-in-a-folder-doesnt-take-you-to-all-notes)]  Esc to go back to all notes from filter](https://linear.app/ideaflow/issue/ENT-1441/pressing-escape-in-a-folder-doesnt-take-you-to-all-notes) - now totally missing on develop? #10-24
- [[[[#maybe Put](https://linear.app/ideaflow/issue/ENT-1506/put-back-the-back-to-all-notes-button)back](https://linear.app/ideaflow/issue/ENT-1506/put-back-the-back-to-all-notes-button)[h]](#cmnt8) the “<-- back to all notes” link at the top when on a filter. Maybe even have that position:fixed for easier self-onboarding #ttt #10-24  — sounds like this is resolved with general back button](https://github.com/IdeaFlowCo/thoughtstream-web/pull/858/files#diff-2b61f219511570c3d6aa2ffda503b6c645813c071bace232ad5e5d42c2ee43e8R51-R70)?
- Show note menu in inline expansions — e.g. would include ability to “jump to” (show in timeline) #tttt

- Make Jump To easier (1 click vs 2 clicks)? Perhaps swap with Pin, as pin is infrequent, placing Pin in the Menu. ​​#10-24
- [[[Some kind of](https://linear.app/ideaflow/issue/ENT-1507/import-mechanism)import](https://linear.app/ideaflow/issue/ENT-1507/import-mechanism)[i]](#cmnt9) — esp Ability to paste in a bunch of text separated by \n\n—\n\n and have it be split (can be custom option on settings page)

- #p1.5 confirm dialog popping up asking if you want to split multiline note on paste

- [[[[[Mobile](https://linear.app/ideaflow/issue/ENT-993/mobile-keyboard-bar-buttons)keyboard](https://linear.app/ideaflow/issue/ENT-993/mobile-keyboard-bar-buttons)[j]](#cmnt10)[k]](#cmnt11)bar with](https://linear.app/ideaflow/issue/ENT-993/mobile-keyboard-bar-buttons) # and +, and maybe more, e.g. tab. (Also, Create Note button, though that could be floating ); + ? tab button ; maybe long press on button #ttt #10-24
- #tweak hitting " #" (space hashtag)  shouldn't break a + relation ; nor should  ~ and ?, or typing a url #10-24
- #tweak if first line is blank maybe show next non blank line in condensed view. Thoughts? #10-24
- General case collapse note feature #10-24
- Note menu is often hard or impossible to click on, eg if you click on a hashtag, then try to click “expand note” on the first note #10-24

-
- Polish - we could get away with ditching any one of these, but I think we need at least some for the sake of polish:

- Last-mile Mobile-specific UX polish, Maybe make # autocomplete pop up from bottom of screen above keyboard bar like slack or ThoughtStream-ios
- [Back button to maintain scroll position](https://github.com/IdeaFlowCo/thoughtstream-web/pull/858/files#diff-2b61f219511570c3d6aa2ffda503b6c645813c071bace232ad5e5d42c2ee43e8R51-R70)

- [and expansion state](https://linear.app/ideaflow/issue/ENT-1508/general-back-button-should-keep-scroll-and-expansion-state) after hashtag filter  #10-24? Is this hard?

- [Ability to copy all notes in the current filter, esp on mobile[l]](#cmnt12)
- [[Closer to full text index search](https://linear.app/ideaflow/issue/ENT-1509/closer-to-full-text-search) - e.g. searching for @ sign to find all notes with emails doesn't work. Also, i wish i could search within words[m]](#cmnt13) — i searched for "sku" to find "swiftsku" but it swiftsku didn't show up #p1.5
- On iPad, and I am guessing iPhone, it takes two touches to click on and filter by a hashtag

- #P2 (priority 2) Nice sliding left animations for filter by hashtag / back to all notes, like on thoughtstream-iOS
- [[#P2 Link title extraction — e.g. when you paste https://www.bbc.com/travel/article/20220928-mexicos-ancient-unknown-pyramids](https://www.bbc.com/travel/article/20220928-mexicos-ancient-unknown-pyramids) , it would prepend the title, a la Bear, sans markdown. Making it: Mexico's 1,500-year-old unknown pyramids https://www.bbc.com/travel/article/20220928-mexicos-ancient-unknown-pyramids](https://www.bbc.com/travel/article/20220928-mexicos-ancient-unknown-pyramids)
- #P2 First load takes a long time #tweak onboarding flow
- #P2 way to turn a list of items you've selected into checklist (edited)
- “I sometimes also forget whether I made something a hashtag or not so I have to search for both “#community-building” & “community building” ~tara” <> #duplicate searching based on prefix - ~taylor
- #P2 Rename hashtag
-
- #P3 Synonym search

Goal: 10 power users + 100 auxiliary active users

[Late Q[n]](#cmnt14)4 2022
- Explore Audio Capture
- See if iOS native app necessary for speed
- Unlinked references

—-

#legend ?? means J thinks it’s fixed but hasn’t checked
—-

### Top priorities for sprint planning from teammates besides Jacob:

#### Taylor: from #day-to-day pinned note Table stakes

- persistence / sync

- you can’t delete an empty note (fixed in develop)
- [I find I sometimes need to refresh before notes gets pushed and/or pulled (pretty sure this is the sw dying problem, which is in progress](https://linear.app/ideaflow/issue/ENT-1472/sw-should-ask-all-cli-for-the-auth-tokens)).
- [edits inside an expansion aren’t saved (in progress](https://linear.app/ideaflow/issue/ENT-1466/when-an-expansion-is-in-a-bullet-changes-arent-saved))
- [The big red scary error messages that I can’t dismiss is too big red and too scary.[o]](#cmnt15)

- onboarding

- There needs to be some way for new users to discover features. Right now there’s no way to learn the syntax for a spaceship or hashtag. The MVP for this in my mind is a small help section.

- UI/UX

- [[Fix folder jank (see ENT-1468](https://linear.app/ideaflow/issue/ENT-1468/dragging-a-folder-in-sidebar-shouldnt-open-it), ENT-1469](https://linear.app/ideaflow/issue/ENT-1469/after-reordering-folder-on-mobile-it-briefly-skips-back-to-original))
- [Pressing spaceship, note menu, etc shouldn’t pull up keyboard tray. This is reeeeally annoying(in progess](https://linear.app/ideaflow/issue/ENT-1457/on-mobile-pressing-a-spaceships-and-shouldnt-open-the-keyboard))
- Jump to timeline not working on mobile (fixed in develop)

- Search

- [Sort by relevance (in develop branch for search and in progress](https://linear.app/ideaflow/issue/ENT-1463/sort-spaceship-suggestions-by-relevance) for “+” suggestions)

- Reading / navigation / exploration

- Notes in Reference section need to be interactive just like a regular note (in progress)

-

### Thoughts on Tradeoffs for Sprint Planning
Jacob: i’m ok ditching folder polish for MVP launch. I think we could get people on the app without folders at all if needed. Of course want to fix soon

#

#

#
——

# 2022-08-05 Roadmap
Q3 2022
- Offline (polish)
- Fast Load Time
- Condensed View
- Reverse relations

- Bug fixes
- UX tweaks

Goal: 10 power users + 100 auxiliary active users

        Q4 2022
- Explore Audio Capture
- See if iOS native app necessary for speed

——
Hackathon ideas:
[Taylor goal /ankify or related; a la https://davidbieber.com/tags/spaced-repetition/](https://davidbieber.com/tags/spaced-repetition/) – taylor attached to anki

Medium term priorities:
[Taylor Jacob Medium Term Priorities #Conversation Aug 5 2022](https://docs.google.com/document/d/1nj8owotUACVoAgz_x3a6DT9-CaFexbviOc3bSQWt2xI/edit)

# Bat-Jacob 2022-04-29 Features

### Most Important
Offline – offline shipped best guess — next week

Condensed
Reverse relations inline

? leave-on audio notes like otter.ai

Ability to copy paste in text

Bug fixes – eg expand relation after filter

Back button accurate position

### Important
Bug fixes “Jump to” working in timeline
scroll position history — back button — @ and ~ — fix bug
share sheet - way to copy all notes on same screen
keeping newline divisoins in refs
audio notes - bat thinks won’t matter till way later
thinking users absolutely need suggestions like entanglement
ability to include hash in refs
Auto url title extraction

### Kinda Important
? 1+ references notes colored differently
bug fixes
ios siri thoughtstream xyz
way to take photo
~ and @ shorthand for notetaking
autocomplete in search bar
popup for quick capture - not fundamental

—

—

—

[[#v1.1](#h.tb88c1r36kke)1](#h.tb88c1r36kke)
[[Intro](#h.kw7wruyxzx2d)1](#h.kw7wruyxzx2d)
[[Background on Types of Notetaking](#h.17uknu1iql03)2](#h.17uknu1iql03)
[[Timeline](#h.26yfi1o39d8e)2](#h.26yfi1o39d8e)
[[---](#h.qher2hv81p2y)5](#h.qher2hv81p2y)
[[#v0.1 (f.k.a Current)](#h.4olidnbd1mcn)7](#h.4olidnbd1mcn)
[[#Old road maps](#h.5pv01x5mn74j)7](#h.5pv01x5mn74j)
[[Web Product Roadmap](#h.fegmw9rpj4c3)7](#h.fegmw9rpj4c3)
[[Mocks](#h.iby429x4wn2z)8](#h.iby429x4wn2z)
[[Websites](#h.pkyekp2rid4q)8](#h.pkyekp2rid4q)
[[Notes from http://productfeedback.jacobcole.net/](#h.bejapswppnvt)10](#h.bejapswppnvt)
[[Top Priorities for December Alpha Launch/Share to Investors. Also Touchstones #designPrinciple](#h.7ni2z4eh30a5)10](#h.7ni2z4eh30a5)
[[Detail Breakout examples (more tweaks below)](#h.482w0lnxp3zd)10](#h.482w0lnxp3zd)
[[Marketing and Communications](#h.5jimmbhs1gqk)10](#h.5jimmbhs1gqk)
[[Press Release Workplan](#h.plssoggagwxu)10](#h.plssoggagwxu)
[[Positioning Prompt #1](#h.gdt4e8f1csm8)11](#h.gdt4e8f1csm8)
[[Help Wanted](#h.s9wknfyldns8)11](#h.s9wknfyldns8)
[[Roadmap](#h.zbh6k952bzs5)11](#h.zbh6k952bzs5)
[[Team Pulse](#h.htshbom7ez5b)11](#h.htshbom7ez5b)
[[Financials](#h.rd66dr25k2y3)11](#h.rd66dr25k2y3)

#

# #v1.1
- Reference

All items are tentative in order/timeline. Items followed by a ? indicates very tentative order.
- Development Phases

- Ideaflow Phase 1: the (single-user) Thoughtstream Web Interface

- Ideaflow Phase 1.5: Entanglement-Style Bullet view (attempt 2)
- Ideaflow Phase 1.6a?:  Auto Tagging/Extraction Tools
- Ideaflow Phase 1.6b?:  Augment Chrome Extension

- Ideaflow Phase 2: Collaborative Thoughtstreams – hopes to be as low friction as texting someone!

- Ideaflow Phase 2.1?: List and Suggestion Box View
- Ideaflow Phase 2.2?: Graph/Mind Map View

- [Ideaflow Phase 3: Rich(ish) Collaborative Documents – replace docs like chronicpain.jacobcole.net](http://chronicpain.jacobcole.net)
- Future Plans?

- Command line for the web / third-party output extensions / integration with big co CRMs
- Social network centered around sharing ideas
- Web crawling + manual effort to create a structured, queryable version of all the Web
- “The Annealing Machine”
- Ideaflow as primary filesystem

- Everything gets a URL

## Intro
- Ideaflow is a large vision that will contain many distinct but ultimately interconnected products

- [What we are building right now, ideaflow.app](https://ideaflow.app/),  I'm calling Ideaflow Phase 1, or the (single) Thoughtstream Web Interface

- It's built for one purpose: to become your go-to scratchpad to capture ideas, quotes, or resources you come across while moving fast, and that you don’t want to lose
- In MVP form, it only needs to be flat (no hierarchy), though may contain purely visual tab indents in notes

- It's like a “command line for your thoughts”
- Design Principle: it's trying to be like a text file, but just a tiny bit better #designPrinciple

- I also see it as a component part of the interface of future product phases I hope we build

- [e.g. It could become an always-available drop-down at top right of an Entanglement-style bullet view](https://www.youtube.com/watch?v=4feZo9PqTlo)

- Later phases will be discussed below

## Background on Types of Notetaking
- Notetaking is a broad term and refers to a lot of different workflows, including the below.

- 1. Taking notes during a lecture in class. Requires features including the following: Outlining, Drawing – e.g. OneNote/Evernote target this

- 1a. Taking notes while reading a complex philosophy book. Requires Outlining, and ideally Relations – e.g. Roam targets this
- 1b. General shared company meeting notes. Requires Collaboration, Outlining, and at least some way to fudge todos in. Google Docs, Notion target this.

- 2. Keeping a todo list – apps for this range from heavy (Omnifocus), to light (Workflowy, iOS Notes). Ideaflow Phase 1 may support checkboxes etc. incidentally but it’s not the target use case persay.
- 3. Personally quickly jotting down ideas, insights, resources, articles you don’t want to forget; keeping reference lists (e.g. of ideas, quotes, restaurants, epiphanies, insights, articles or comments from various newsfeeds); also queueing up suggestions you want to give to various companies, organizations; things you want to say to various people next time you see them – Ideaflow Phase 1 targets this. Alternatives include iOS notes, Simplenote, Roam (esp. see Daily Notes feature), Slacking yourself, keeping a giant text file, TheBrain.com

- 3a. Very casual shared notes from calls/discussions

- 1:1 calls. Existing workflows: texting each other links, FB messages
- Team Zoom calls. Existing workflows: Initially, Zoom chat, then copy paste to Slack
- Zoom or Clubhouse group discussions/salons; Zoom classes as well. Existing workflows: LinkedIn/FB/Telegram group chat
- Ideaflow Phase 2 hopes to be as low friction for this as texting someone!

- 3b. Slightly more formal notes for interesting group conversations, idea brainstorming sessions at work, etc.  Note that this may be distinct from 1b. “General company meeting notes”.

- [[Zoom or Clubhouse group discussions/salons: Setting up a Google doc with notes like http://salon.jacobcole.net/](http://salon.jacobcole.net/) or http://systematicawesome.jacobcole.net/](http://systematicawesome.jacobcole.net/) . Roam is planning to becoming a tool for this as well.
- Ideaflow Phase 2 ideally hopes to be a tool for this as well, but slightly less important than the 3a. use case. This might wait for Ideaflow Phase 3: Rich(ish) Collaborative Documents

- [[4. Keeping “dossiers” on people (see also https://en.wikipedia.org/wiki/Farley_file](https://en.wikipedia.org/wiki/Farley_file)). Tools that Target this:  getdex.com](https://getdex.com/) CRM, Affinity CRM, Roam (sorta), and Ideaflow Phase 1.5 (Bullet view, will discuss later) will target this.
- [5. Creating high quality reference sources on various topics, like http://chronicpain.jacobcole.net/](http://chronicpain.jacobcole.net/) . Requires precisely the same features as “1b. General shared company meeting notes. Requires Collaboration, Outlining, and at least some way to fudge todos in. Google Docs, Notion target this.” Ideaflow Phase 3: Rich(ish) Collaborative Documents explicitly addresses this

## Timeline

Jan 31
- Ideaflow Phase 1 “Thoughtstream Web”

- Use case: Targets Notetaking Use Case 3

- “3. Quickly jotting down ideas, resources, articles you don’t want to forget; keeping reference lists (e.g. of ideas, quotes, restaurants, epiphanies, insights, articles or comments from various newsfeeds);also queueing up suggestions you want to give to various companies, organizations; things you want to say to various people next time you see them  – Ideaflow Phase 1 targets this. Alternatives include iOS notes, Simplenote, Roam (esp. see Daily Notes feature), keeping a giant text file, TheBrain.com”
- “It's built for one purpose: to become your go-to scratchpad to capture ideas, quotes, or resources you come across while moving fast, and that you don’t want to lose”
- Workflow: Generally, I expect it to be used as an always-open desktop application (separated from Chrome via the Tools >  create shortcut >  “open as window” feature for easy command-tab access)  or iOS home screen native application

- Product Notes

- “In MVP form, it only needs to be flat (no hierarchy), though may contain purely visual tab indents in notes”

- It's like a “command line for your thoughts”
- Design Principle: it's trying to be like a text file, but just a tiny bit better #designPrinciple

- Estimated additional features needed to complete this phase

- [ ] Some minimal onboarding docs, initial text on screen, or tutorial
- [ ] Sundry bug fixes – mostly captured by P1 in Linear, and some of the new ones recently mentioned in #jacob-raw-thoughts

- Target Users

- Super on-the-go notetakers like David Bieber, Alex List, Jacob

- Hypothesis

- [[There exist at least a few (3?) people[p]](#cmnt16)[q]](#cmnt17) that really need better a tool for Use Case 3.

- Complaints about existing tools

-  include: need lower-friction tool than Roam daily notes

- Faster load time on Web than Roam
- Better on mobile than Roam
- Different workflow / fewer extraneous features than Roam

-  “I'm not the person Roam was built for” ~Adam Towers

- Success Condition:   Alpha users will use it a ton over course of 1 mo

- Possible success metrics

- Roam metric: used > 4 days / week
- > 10 actions / day (most session duration numbers are kind of hard to leverage and measure these days. Number of actions are a bit more significant.)
- 20+ notes a week on average
- [[Time: Spending over one hour per week on the app[r]](#cmnt18)[s]](#cmnt19)
- Subjective metrics (e. “I would be very sad if this tool were to go away”)

- [[Note: Perhaps we should suggest people to use other tools for other workflows[t]](#cmnt20)[u]](#cmnt21), E.g. Workflowy for outlining class notes, and other todo trackers like omnifocus for tasks, so we can isolate this behavior?

- Possible Outcome 1:

- I hypothesize that finishing just the P1 features – which I see as the bare minimum for a quality app experience — will be sufficient to achieve this.

- Possible Outcome 2:

- Alternate hypothesis: the subset of users who currently like the iOS app won’t be satisfied with mobile web, and demand mobile web improvements OR sync with iOS app.

- Jacob, David Bieber, Danish blockers primarily around snappy/quality experience

- Navigation / design tweaks would be needed esp. on iOS e.g. Hashtags bar, clicking on hashtags to filter
- Note: to get me (Jacob) personally to fully migrate from Thoughtstream iOS would additionally require relations, and possibly a few more changes

- Possible Outcome 3:

- Nobody actually likes the workflow of having a giant text file they prepend thoughts to. Maybe we skip to trying out Phase 1.5 Bullet View, then?

- Feb 28

- Product goals:

- Mainstay Improvements

- Very high-quality iOS experience (e.g. # on bar above keyboard), synced with web app, whether its wrapped react native, or Swift
- Single user multi-device / multi-window sync. It doesn't have to be real time but maybe could even just pull every 3 seconds?
- Relations

- Implement bidirectional relations/improve relation experience
- Make relations work in search bar

- Great onboarding tutorial/walkthrough teaching the desired workflow
- Changelog

- If time, version history?

- New Features

- Relations

- Inline expansion of relations in ideaflow.app (I’m calling Thoughtstream Web).

- Not necessarily inline expansion of tags @’s and ~’s, but possibly – it would be great to experiment  

- UX improvement experiments

- e.g. Zen Mode: Mode where each new day creates many line breaks so you don't see past day’s notes on the screen, or you can click an expand button on any note to have it pop up to the size of a near-full-screen modal, requested esp. by Ben

- [Phase 1.5: Entanglement-style bullet view](https://www.youtube.com/watch?v=4feZo9PqTlo) interface experiment

- Highly requested by VC’s
- Targets Notetaking Use Case 4

- [[“4. Keeping “dossiers” on people (see also https://en.wikipedia.org/wiki/Farley_file](https://en.wikipedia.org/wiki/Farley_file)). Tools that Target this:  getdex.com](https://getdex.com/) CRM, Affinity CRM, Roam (sorta), and Ideaflow Phase 1.5 (Entanglement view, will discuss later) target this.”

- Built off of core Thoughtstream Web codebase; ideally, minimal changes needed.
- Design Possibilities:

- View could be accessible via separate tab or menu
- Thoughtstream Web interface could become an always-available top righthand bar drop-down when this view is active

- Key features

- Like Thoughtstream Web, but with the following changes

- Starting to type a new note, e.g. “Ben Williams”, would initiate autocomplete.
- Relation labels

- e.g.

- Ben Williams
- Founder of: Auxparty
- Lived in: Colorado

- May require us to support labels inside <>’s on Thoughtstream Web, which isn’t a bad thing.

-  E.g. “He who has a why to live can bear almost any how”  ~Nietzsche <contrapositive of> “He who stands for nothing Falls for anything” ~Martin Luther King
- May require design work on mobile

- No date dividers by default

- Target Users

- People who need to network and remember people

- CEO’s like Vlad from Lunchclub and their Chiefs of Staff
- VCs like GFC’s Don Stalter, First Round’s Bill Trenchard
- Superconnectors like Aku and Jacob
- People with memory problems who also need to network: e.g. Sigward, who runs an accelerator

- Success Condition:  Alpha users will use it a ton over course of 1 mo

- Possible success metrics

- Roam metric: used > 4 days / week
- > 10 actions / day (most session duration numbers are kind of hard to leverage and measure these days. Number of actions are a bit more significant.)
- 20+ notes a week on average
- [[Time: Spending over one hour per week on the app[v]](#cmnt22)[w]](#cmnt23)
- Subjective metrics (e. “I would be very sad if this tool were to go away”)

- Ops Tasks:

- Import Jerry/ Mark Trexler’s Brains

- Onboard Jerry
- Onboard Mark carranza?

- Mar 30

- Mainstay Improvements

- Offline sync with iOS app

- New Features
- Tweaks

- Experiment with treating separate lines of any note as implicit bullets, in a visually subtle way – jacob has mocks on this
- Child notes / true hierarchical outlining, a la Workflowy

- Could be built off of Inline expansion of relations
- Would include features like zooming in like Workflowy has, Or maybe we would Implement zooming in with a modal

- Thoughtstream Web interface could become an always-available top righthand bar drop-down when you're zoomed in?

- Ideaflow Phase 1.6a?:  Auto Tagging/Extraction Tools

- Audio note support and auto transcription

- Reverse voice search

-  automatic extraction of title from URL
-  automatically tag link to article as #article #biology
-  process images / photos

- OCR
-  object recognition and searchability
-  Screenshots

- E.g.  Facebook post for Twitter tweet extract entities

- Automatic backup of any linked web page

- Phase 2: Collaborative Thoughtstreams

- Use cases:

- “3a. Very casual shared notes from calls/discussions”

- 1:1 calls. Existing workflows: texting each other links, FB messages
- Team Zoom calls. Existing workflows: Initially, Zoom chat, then copy paste to Slack
- Zoom or Clubhouse group discussions/salons; Zoom classes as well. Existing workflows: LinkedIn/FB/Telegram group chat
- Ideaflow Phase 2 hopes to be as low friction for this as texting someone!

- “3b. Slightly more formal notes for interesting group conversations, idea brainstorming sessions at work, etc.  Note that this may be distinct from 1b. “General company meeting notes”.”

- [[Zoom or Clubhouse group discussions/salons: Setting up a Google doc with notes like http://salon.jacobcole.net/](http://salon.jacobcole.net/) or http://systematicawesome.jacobcole.net/](http://systematicawesome.jacobcole.net/) . Roam is planning to becoming a tool for this as well.

- Ideaflow should be the buddy tool every group chat – Create a Collaborative Thoughtstream for each one

- E.g. anytime you have a big facebook or telegram group chat
- Every community (e.g. SF Salon,  StartX) should have an ideaflow  
- Even every 1:1 chat, e.g. Jacob & JM’s texting history
- Each should have a collaborative thoughtstream that is distinct from a chat, because the chat may include transient information like “hey are you here yet”

- Features:

- Ideally, typing #book Eye of the World in a facebook group chat would cause it to get persisted to the group’s Ideaflow

- [This may be possible a la http://texts.com/](http://texts.com/)
- [Future: Eventually we should probably build our own chat app to compete with FB & telegram ; Ideally it would be a new multichat client like texts.com](http://texts.com/)

- [Should have memorable, typable urls, like sfsalon.ideaflow.app](http://sfsalon.ideaflow.app)
- These should be instant to create

- I bought the domain if.new, kinda like docs.new :-)
- Should be a list of all the created ones somewhere

- Maybe like shared.ideaflow.app or thoughtstreams.io could be the url? And it would also of course have a big friendly create new button

- [We should have a “people tab” that’s basically a spreadsheet like http://people.worldquestguild.connectordocs.com/](http://people.worldquestguild.connectordocs.com/)  where people can fill in their interests

- Biz Ops Work

- [Build Global Idea Bank](http://globalideabank.jacobcole.net/) and migrate onto Ideaflow

- Build database of all projects going on at MIT, Stanford, and other universities and migrate onto Ideaflow

- April 30

- Phase 3: Collaborative Rich Documents

- Use Case:

- [“5. Creating high quality reference sources on various topics, like http://chronicpain.jacobcole.net/](http://chronicpain.jacobcole.net/) . Requires precisely the same features as “1b. General shared company meeting notes. Requires Collaboration, Outlining, and at least some way to fudge todos in. Google Docs, Notion target this.”

- Features

- Headings and subheadings, some level of rich text, real-time collaborative text editor. Etherpad or Hackpad (or heck, Dropbox paper) would be a fine base functionality set. But I’d want a view where I can filter the doc, maybe in a pop-up by tags

- 3 Differences between thoughtstream web editor and a minimalist docs editor

- Hierarchies (achievable natural as an extension of inline expansion)
- “Different” Features

- Linkifying hyperlinks
- Headings

# ---

#

# #v0.1
- Jacob’s HW

- Background: Notetaking is a broad term and refers to a lot of different workflows, from taking notes during a lecture in class, to keeping a todo list, to keeping reference lists (e.g. of ideas, quotes, restaurants, epiphanies, insights, articles or comments from various newsfeeds)
- Feb 1

- [[[My hope is to be able to test the hypothesis that there exist at least a few people[x]](#cmnt24)[y]](#cmnt25) that really need an ultra low friction tool especially for the third [z]](#cmnt26)category, and will use such a tool a ton, as evaluated by, after one month of using the tool, any of the below:

- Subjective metrics (e. “I would be very sad if this tool were to go away”)
- 20+ notes a week on average
- [[Spending over one hour per week on the app[aa]](#cmnt27)[ab]](#cmnt28)

- [[Perhaps we should suggest people to use other tools for other workflows[ac]](#cmnt29)[ad]](#cmnt30), E.g. Workflowy for hierarchical outlining, and other todo trackers for tasks, so we can isolate this behavior?
- I hypothesize that finishing just the P1 features – which I see as the bare minimum for a quality app experience — will be sufficient, to achieve this.

- Alternate hypothesis: the subset of users who currently like the iOS app won’t be satisfied with mobile web, and demand mobile web improvements OR sync with iOS app.
- Aside: to get me (Jacob) personally to fully migrate would additionally require relations, and possibly a few more changes

Ben feedback:
Here’s my feedback:
Background: Notetaking is a broad term and refers to a lot of different workflows,
You listed three workflows, but I’m still not 100% clear on what workflows we are targeting and which ones we are not supporting. It would be awesome to have a clear guideline on that so we can all be on the same page for testing purposes
--------
test the hypothesis that there exist at least a few people that really need an ultra low friction tool especially for the third category
[who do we think these people are? Where do you think we can find them? What tools are they currently using to try to solve their needs? What are those tools missing? How many people is a few?[ae]](#cmnt31)
--------
 “Perhaps we should suggest people to use other tools”
If we can define the use case we are supporting, I think it makes it much easier to do this
--------
Alternate hypothesis: the subset of users who currently like the iOS app won’t be satisfied with mobile web, and demand mobile web improvements OR sync with iOS app.
How many users on mobile do we have that currently meet the all three criteria that you listed?
 Subjective metrics (e. “I would be very sad if this tool were to go away”)
20+ notes a week on average
Spending over one hour per week on the app
[Since we don’t track anything on mobile, do we have a way to know this?[af]](#cmnt32)

# [#Old road maps[ag]](#cmnt33)

## Web Product Roadmap
Q3 2020
Q4 2020
Dec 2020
 make great thoughtstream experience
         perfect text editing, fast loading, sync mobile and web
                 launch to Alpha users like David Bieber, Danish, Andrew P, Ali

Q1 2021
        Make great ontology editor (bullet view) experience
         make great subdomain+docs  experience

Q2 2021

After Q2 2021
Integration with Google Docs

### Mocks
         figma sketch

Week of Nov 4 - 6
Week of Nov 9 - 13
Week of Nov 16 - 20

11/4
11/5
11/6
11/9
11/10
11/11
11/12
11/13
11/16
11/17
11/18
11/19
11/20
Milestones

Finalize Press Kit
Contact reporter for exclusive

Briefing with reporter

Priming email to F/F
Press Release Launch

Key Areas
Press Kit

Finalize Press Kit

Press relations

ID reporter
Contact Reporter

Briefing with reporter

Distribution

-

Social media

Others

Team Responsibilities
Jacob
Review positioning
Review PR draft
Approve Press kit

Briefing prep
Briefing prep
Briefing

Vince
Positioning
Positioning
Draft PR
Press Kit edits
Refine blog
Prep Jacob
Prep Jacob

JM
Positioning
Positioning
Draft PR
Press Kit edits
Refine blog

Arielle
- Review positioning
- ID reporters
- Review positioning
- ID reporters
Review blog
- Select reporters
Contact reporter
Prep Jacob
Prep Jacob

Christine

## [Websites[ah]](#cmnt34)
[Ideaflow.io (homepage)](https://www.ideaflow.io/).
https://ideaflow.app/
https://apps.apple.com/us/app/thoughtstream/id1330828366
Augment chrome extension

# [Notes from http://productfeedback.jacobcole.net/](http://productfeedback.jacobcole.net/)

### [Top Priorities for December[ai]](#cmnt35) Alpha Launch/Share to Investors. Also Touchstones #designPrinciple

- [[Make the app holistically[aj]](#cmnt36) snappy, slick, not buggy[ak]](#cmnt37)

- The Lowest friction knowledge capture
- High quality text editor experience
- Ben, Danish, Jacob & everyone use the app

- Gee-wow touches

Target people:
- Bill trenchard (investor, new user),
- Danish (uses Web app on desktop some, thoughtstream native app on iOS),
- Jacob  (uses Web app on desktop, thoughtstream native app on iOS) ,
- David Bieber (uses thoughtstream iOS native, Roam on desktop)
- Ali Tarraf (mgmt consultant)

#### Detail Breakout examples (more tweaks below)
Lowest friction knowledge capture
- Mobile

- Quick login and stay logged in on mobile
- Bottom up autocomplete on mobile
- Bar with # and @ etc

- Instant load time

High quality text editor experience
- [iOS web app has to feel as good as native[al]](#cmnt38)

- [No “position is undefined” errors or other[am]](#cmnt39)
- [No need for login each time[an]](#cmnt40)
- [Touch[ao]](#cmnt41) bar for # @ ~ ?

- No typing lag
- Cursor jumps to before tag when creating tags on mobile

Ben & everyone use the new app actively
- [Jacob, Danish[ap]](#cmnt42) blockers primarily around snappy/quality experience

- Navigation / design tweaks eg clicking on hashtags to filter

- [Can’t start losing content when logged out with tiny warning of “JWT[aq]](#cmnt43) expired”

[Gee-wow touches[ar]](#cmnt44)
- Inline expansion
- Import Jerry/ Mark Trexler’s Brains

Future/Defer
[?never lose anything[as]](#cmnt45), history? – export covers this?
Offline mode
Changelog
Sort by Date

---

# [Marketing and Communications[at]](#cmnt46)

### Press Release Workplan

Week of Nov 4 - 6
Week of Nov 9 - 13
Week of Nov 16 - 20

11/4
11/5
11/6
11/9
11/10
11/11
11/12
11/13
11/16
11/17
11/18
11/19
11/20
Milestones

Finalize Press Kit
Contact reporter for exclusive

Briefing with reporter

Priming email to F/F
Press Release Launch

Key Areas
Press Kit

Finalize Press Kit

Press relations

ID reporter
Contact Reporter

Briefing with reporter

Distribution

-

Social media

Others

Team Responsibilities
Jacob
Review positioning
Review PR draft
Approve Press kit

Briefing prep
Briefing prep
Briefing

Vince
Positioning
Positioning
Draft PR
Press Kit edits
Refine blog
Prep Jacob
Prep Jacob

JM
Positioning
Positioning
Draft PR
Press Kit edits
Refine blog

Arielle
- Review positioning
- ID reporters
- Review positioning
- ID reporters
Review blog
- Select reporters
Contact reporter
Prep Jacob
Prep Jacob

Christine

### Positioning Prompt #1

## Help Wanted
- [General: If you know of any influential "supercurator" individuals who keep an enormous personal knowledge base (like Jim Keravala](https://www.linkedin.com/in/keravala/)) that we might want to build relationships with, please let us know. We’re seeking to create “off-the-shelf” knowledge sets that users can benefit from on day one, and to establish inroads into relevant organizations these folks have connections with.
- Hiring: Progressing well, yet not done. We’ve been integrating a new incredible engineering teammate over the last month: Ben Williams, full stack engineer and founder of the popular social music experience site AuxParty, and the team is gelling well. Looking especially for another excellent Javascript and iOS engineer, if you know any star ex-founders, for instance, or operators who might know such founders. Job descriptions.

- [iOS Engineer](https://www.ideaflow.io/ios-engineer)
- [Full Stack Engineer](https://www.ideaflow.io/full-stack-engineer)
- [Product Designer](https://www.ideaflow.io/product-designer)
- [NLP/Machine Learning Engineer](https://www.ideaflow.io/ml-engineer)

## Roadmap
- [If you know of any influential "supercurator" individuals who keep an enormous personal knowledge base (like Jim Keravala](https://www.linkedin.com/in/keravala/)) that we might want to build relationships with, please let us know. We’re seeking to create “off-the-shelf” knowledge sets that users can benefit from on day one, and to establish inroads into relevant organizations these folks have connections with.

## Team Pulse
- Total Employees = 3 full time (really), + 2 (parttime david)+ 1 (albert), Contractors FT (1 JM) (contractor occasional: evan, vince, jen, aku, ?jenni), ,  [#]
- Total Employees = [#]
- New hires or losses, team mood, wins or concerns on the culture front.

## Financials
- Burn rate: ~$180k/mo (on budget)
- Runway: ~3 years based on our current roadmap

------

# Spencer Jacob Call Notes

## Foundations
snappy experience
team that is energized creative hacking enjoying working
together
iterating rapidly with "users" internal or external
--
humanity: could get all basic needs met in 1 day with perfect coordination
even the big societal disagreements are tips on the iceberg

--

Could get substantial market share with just

---

Could get a lot of happy users just by cloning things

Prefers - 10x value

---

Foundation: basic text file sync ios and web app

        Spencer: native mobile app is a must at least ios
                ? Fast knowledge capture e.g. rec?
        Some sort of bullet view

---

Can it be used by someone who is dictating/ quadruplegic

-----------

0. make sure relations work in the search bar when you click on them  as per evan’s mock. Weird bugs atm.
0.1 Can we pretty please have a mode where reverse relations are created automatically

“What man actually needs is not a tensionless state but rather the striving and struggling for a worthwhile goal, a freely chosen task. What he needs is not the discharge of tension at any cost but the call of a potential meaning waiting to be fulfilled by him.” ~Viktor Frankl #quote <> “He who has why to live can bear almost any how…

-----------

#book Shabhala – the sacred path of the warrior
#spiritualWarriorship

-----------

                #yogaPerson spencer kim

-----------
“He who stands for nothing falls for anything” ~Martin Luther King #quote <> “He who has a why…

-----------

#book Stealing Fire

-----------

        “He who has a why to live can bear almost any how” ~Nietzsche #quote
<> “He who stands for nothing…
<> “What man actually needs is not a tensionless
-----------

- Inline expansion of relations as per Evan mock (other part) and jacob-ts-listview’

- Labeled relations

- If it’s not too tough to implement, from a logical progression standpoint, we should make it so that

Charlie Cheever <investor of> Ideaflow is typable in thoughtstream
When you expand (inline expansion) it might say:

--------------------
Charlie Cheever <investor of> Ideaflo...
| + investor of: Ideaflow – Company founded at MIT <...>... <early employee> Bat M...
| + early employee:Bat Manson
| …
      Literal text matches (“Unlinked references”)
      | Charlie Cheever <cofounder of> Quora
      | Charlie Cheever <founder of> Expo
      | a cool ios hacker is Charlie Cheever, who lives in palo alto  <> Feross

-----------------------
Ideaflow – Company founded at MIT  <investor> Charlie…<early employee> Bat M...

----------------------

Unlinked references with aggregation (Spencer version)

--------------------
Charlie Cheever <investor of> Ideaflo...
| + investor of: Ideaflow – Company founded at MIT <...>... <early employee> Bat M...
| + early employee:Bat Manson
| …
      Literal text matches (“Unlinked references”)
      | Charlie Cheever <cofounder of> Quora...<founder of> Expo...

Unlinked references with aggregation (jacob version dirty)

--------------------
Charlie Cheever <investor of> Ideaflo...
| + investor of: Ideaflow – Company founded at MIT <...>... <early employee> Bat M...
| + early employee:Bat Manson
| …
     Relations derived from literal text matches
|investor of: Ideaflow
|cofounder of: Quora
|founder of: Expo
    Literal text  “contains” matches (“Unlinked references”)
      | a cool ios hacker is Charlie Cheever, who lives in palo alto  <> Feross

Unlinked references with aggregation (jacob version clean)

--------------------
Charlie Cheever <investor of> Ideaflo...
| + investor of: Ideaflow – Company founded at MIT <...>... <early employee> Bat M...
| + early employee:Bat Manson
| - investor:Charlie Cheever
|investor of: Ideaflow
     Relations derived from literal text matches
|cofounder of: Quora
|founder of: Expo
    Literal text  “contains” matches (“Unlinked references”)
      | a cool ios hacker is Charlie Cheever, who lives in palo alto  <> Feross

--------------------
Charlie Cheever<investor of> Ideaflo...
| + investor of: Ideaflow – Company founded at MIT <...>... <early employee> Bat M...
| + early employee:Bat Manson
| - investor:Charlie Cheever
|investor of: Ideaflow
     Relations derived from literal text matches
|cofounder of: Quora
|founder of: Expo
    Literal text  “contains” matches (“Unlinked references”)
      | a cool ios hacker is Charlie Cheever, who lives in palo alto  <> Feross

- Labeled relations more like bullet view

Charlie Cheever <investor of> Ideaflo...
|  Ideaflow  – Company founded at MIT

Charlie Cheever <investor of> Ideaflo...
|investor of: Ideaflow, Forge, Quora

- Aggressive autocomplete of WHOLE NOTE (TOGGLABLE) – this is the possibly defining difference between the “2 windows” in jacob’s workflow

Below is with “Entanglement Mode” on – aggressive autocomplete

------------------
Charli

------------------
+ Charlie Cheever
------------------

+ Charlie Cheever<investor of> Ideaflo...

- Charlie Cheever<investor of> Ideaflo…
|investor of:Ideaflow
|friends with: Mark Zuckerberg
|founder of: Expo

Key difference between entanglement And thought stream as it is right now is how aggressive the autocomplete is

Jacob Cole:
        The point about being two views is almost a distraction by the way – as long as you’re able to have two windows open of the same application you don’t even need to views I don’t think for my optimal workflow
        All we need is basic in line expansion (+ unlinked references as Showable)
        *2 views
        Context and local scoping is a future point we can discuss
        Which I internally think of as a special “child-of” relation
        Anyway we can discuss Monday
        2pm doable?
Spencer Kim:
        thanks, that’s helpful
        Can we do 230?
Jacob Cole:
        Ya
        (Last point that we can go over in our next discussion: because I see child relationships as a special case of other relationships, I think it probably actually makes sense to support labeled relation ships before child relationships)

-

a cool ios hacker is Charlie Cheever, who lives in palo alto  <> Feross

ios hackernamedCharlie Cheever, wholivesinpalo alto

Who ( named( subject: ios hacker, direct object: Charlie Cheever), in(lives, palo alto) )

#tt #catchup brody <> spencer kim   #linguistics #neurobiology

- 1 1

1+1

1 1 +

### Scratch Backup

- Labeled relations

- If it’s not too tough to implement, from a logical progression standpoint, we should make it so that

Charlie Cheever <investor of> Ideaflow is typable in thoughtstream
When you expand (inline expansion) it might say:

--------------------
Charlie Cheever <investor of> Ideaflo...
|  Ideaflow – Company founded at MIT <...>...

-----------------------
Ideaflow – Company founded at MIT  <investor> Charlie…

----------------------
- Labeled relations more like bullet view

Charlie Cheever <investor of> Ideaflo...
|  Ideaflow  – Company founded at MIT

Charlie Cheever <investor of> Ideaflo...
|investor of: Ideaflow, Forge, Quora

### Team Questions for next Roadmap Iteration
- Business Strategy

- viable paths however
- Key Metric

- Number of Power Users “Earlyvangelists”

- Number of users who login more than four days/week (and take at least one write or search action?)

- Strategy

Bat
- Would appreciate more business considerations rather than product features, need more Macro considerations on how to get to a good Series A
- Specific Questions: Key considerations for Series A? Will we do a Series A? How will we take into account user feedback & priority? How many users by when? What profile of users? Do we plan to sell / when will we sell? If you knew very little about the product & everything about the market, what would you do?
- Bat: Let's say users are overwhelmed by cognitive load presented by text file UI, this means we have to change the product which can make the product roadmap collapse on itself. Always risky to have a 6 month product roadmap, which is why startups are great & big corps are shit. I know it's important that we should have big opinions around product features, but this is a common cause for company collapse, for no one is paying attention to product-market fit.

- Investor Expectations for Shone were very misaligned which is why they skipped on the series A
- Jacob: Yes, idea is likely 1 or 2 of our investors would pre-empt a series A if they saw a few thousand users excited / if investors were excited using the app themselves. Majority of investors is 10k MAUs

Spencer
- It would be helpful if you built a completely different document than this
- Spencer’s recommendation from slack:

- Concretely what would be helpful to understand is the business decision tree and I think something as simple as a chart or quick bullet points with some timelines and very high-level descriptions would be awesome
- i.e. what exactly we are aiming for? What steps we are planning to get there? and along that path how we know (via metrics or otherwise) whether to keep moving forward or to try another direction
- This would help answer some questions I have like — what is the current hypothesis we are trying to validate? and which user cohort does that target? Specifically what is our strategy for reaching and onboarding these users (PR?, personal networks)? What metrics (# of users, notes per day, etc.) do we need to reach to know we’ve validated this hypothesis? What is the goal after we get the traction we want (e.g. series A)? Instead if the experiment flops, which path do we go down and to what degree does that delay/change our goals?

Ben
- Re: Background: Notetaking is a broad term and refers to a lot of different workflows,

- You listed three workflows, but I’m still not 100% clear on what workflows we are targeting and which ones we are not supporting. It would be awesome to have a clear guideline on that so we can all be on the same page for testing purposes

- Re: test the hypothesis that there exist at least a few people that really need an ultra low friction tool especially for the third category

- Who do we think these people are? Where do you think we can find them? What tools are they currently using to try to solve their needs? What are those tools missing? How many people is a few?

- Re:  “Perhaps we should suggest people to use other tools”

- If we can define the use case we are supporting, I think it makes it much easier to do this

- Re: Alternate hypothesis: the subset of users who currently like the iOS app won’t be satisfied with mobile web, and demand mobile web improvements OR sync with iOS app.

- How many users on mobile do we have that currently meet the all three criteria that you listed?

- Subjective metrics (e. “I would be very sad if this tool were to go away”)
- 20+ notes a week on average
- Spending over one hour per week on the app

- Since we don’t track anything on mobile, do we have a way to know this?

# RPC Paper2Graph

- case insensitive

- https://stackoverflow.com/questions/13439278/running-a-case-insensitive-cypher-query
- https://neo4j.com/docs/cypher-manual/current/clauses/where/#case-insensitive-regular-expressions
- Doesn’t use indexes

- Hashes + slug in filename when you click save to neo4j

- Track sources array on ea neo4j node and edge

- [Run job on existing neo4j to deduplicate case-sensitive matches, log list of what connections had been missed[au]](#cmnt47)

[[a]](#cmnt_ref1)not possible afaik
[[b]](#cmnt_ref2)kk. curious if it would be doable if we put the app in a react native wrapper?
[[c]](#cmnt_ref3)yes.
[[d]](#cmnt_ref4)this is a duplicate, search is not working at all on develop
[[e]](#cmnt_ref5)so relevance sorting? Finally? Same for search then?
[[f]](#cmnt_ref6)I personally still prefer date sorting, with prefix matches lifted -- when we tried relevance sorting on thoughtstream ios, I found it hard to find recently created notes. I'm open to trying though
[[g]](#cmnt_ref7)What you spec is relevance sorting imho. Aka a ranking computed on length and position of the match (title/starting by/containing), frequency and freshness. What do you think relevance sorting would do differently from what you suggest?
[[h]](#cmnt_ref8)Do you want 2 buttons? This one and the general back button taylor has been working on?
[[i]](#cmnt_ref9)we discussed and said that "\n--\n" was a better note splitter criteria. If you want to convert from \n\n to "\n--\n" you only need one search and replace.
[[j]](#cmnt_ref10)not designed it will be hard to implement something in the next month if we dont even have polished mockups with open ended question
[[k]](#cmnt_ref11)I'm content with Sam's design https://www.figma.com/file/YBUbNIHBVfV6MT3aiLez3z/Visual-design-upgrade?node-id=3%3A31358
What do you think?
[[l]](#cmnt_ref12)if only we kept the select all to work as intended...we wouldnt have to surface a barely used button to the interface :)
[[m]](#cmnt_ref13)+1
[[n]](#cmnt_ref14)q3 is already over. Delivering a correct audio capture experience is like 6 months - it is its own app. Otter.ai took several years to provide such an experience...
[[o]](#cmnt_ref15)The main thing I was getting at with this is that sometimes these messages a) can't be dismissed and b) don't provide suggested solution (e.g. graphql one). I agree we should surface errors to users e.g. to tell them something is wrong and they should refresh, but they need to be somewhat interpretable by users and have provide steps to resolve (even if the step is just: "contact taylor@ideaflow.io for assistance)
[[p]](#cmnt_ref16)how many roughly 5 / 10 / 100 ?
[[q]](#cmnt_ref17)3?
[[r]](#cmnt_ref18)most session duration numbers are kind of hard to leverage and measure these days. Number of actions are a bit more significant.
[[s]](#cmnt_ref19)Done
[[t]](#cmnt_ref20)The market of users ready to take their notes in more than one place is intuitively under 1% imo. Sounds risky to address/target/create such a demo.
Would like to check numbers on that
[[u]](#cmnt_ref21)How about people who use iOS notes for ideas and reference lists but OneNote for lecture notes?
[[v]](#cmnt_ref22)most session duration numbers are kind of hard to leverage and measure these days. Number of actions are a bit more significant.
[[w]](#cmnt_ref23)Done
[[x]](#cmnt_ref24)how many roughly 5 / 10 / 100 ?
[[y]](#cmnt_ref25)3?
[[z]](#cmnt_ref26)what is the 3rd category, keeping reference lists?
[[aa]](#cmnt_ref27)most session duration numbers are kind of hard to leverage and measure these days. Number of actions are a bit more significant.
[[ab]](#cmnt_ref28)Done
[[ac]](#cmnt_ref29)The market of users ready to take their notes in more than one place is intuitively under 1% imo. Sounds risky to address/target/create such a demo.
Would like to check numbers on that
[[ad]](#cmnt_ref30)How about people who use iOS notes for ideas and reference lists but OneNote for lecture notes?
[[ae]](#cmnt_ref31)David Bieber, Alex List, Ben San Souci, me, and several others at least
[[af]](#cmnt_ref32)we at least have David Bieber, Alex List, Ben San Souci, me, and several others using thoughtstream to these criteria @ben@ideapad.io Can look into metrics
[[ag]](#cmnt_ref33)Should we ignore this?
[[ah]](#cmnt_ref34)?
[[ai]](#cmnt_ref35)we launch to investors then! Need to reconcile with the first page
[[aj]](#cmnt_ref36)please detail what you mean by holistically snappy. Are we talking about performance of the whole app?
At Apple we say make it work then make it beautiful then make it fast.
[[ak]](#cmnt_ref37)we usually dont write down not buggy. I know its not the intent, but that comes of as condescending and uneducated. Nobody in a team purposely make something buggy. It's always a question of threshold.
99% of apps have bugs, 99.99% of startup products have bugs and they still makemoney... so not buggy cannot be a goal per say.
Usually we dont talk about bug fixes in roadmaps and let engineering fix what has to be fixed
[[al]](#cmnt_ref38)as our native? please detail.
Its very subjective, I know for instance i would never use the current mobile app, it has too many undefined behavior and functional quirks that i can never be in the flow with it
[[am]](#cmnt_ref39)so... no error? :)
[[an]](#cmnt_ref40)duplicate of the paragraph above
[[ao]](#cmnt_ref41)is a duplicate of the paragraph above
[[ap]](#cmnt_ref42)could we get the feedback from danish eventually? From what I read he had issues with the color scheme...
[[aq]](#cmnt_ref43)Is a bit small to be in a roadmap. You have a team of 3 and a roadmap is for 1 quarter, so south of 200 days of work. This is half a day of work. What I read is more an product principle: never loose notes, which should be an invariant all among our journey. What do you think?
[[ar]](#cmnt_ref44)those are more roadmap worthy, they only miss the why and associated detail/specs/analysis
[[as]](#cmnt_ref45)sounds like a dup of can't start loosing content, or is it different?
[[at]](#cmnt_ref46)already present in the page before?
[[au]](#cmnt_ref47)There were 4 nodes that had duplicates