[codingchallenge.jacobcole.net](http://codingchallenge.jacobcole.net)

# IdeaFlow JavaScript Coding Challenge

# Hashtag (#), People (@), and Relations (<>)  Autocomplete in Draft.js

# UPDATE 2023 – do the following except with http://prosemirror.net/

##

## New and Improved Challenge (as of 10/2020)
https://github.com/IdeaFlowCo/template-autocomplete

## Wireframes
https://drive.google.com/a/ideapad.io/file/d/0B-I9KaLn57eRWFNuU3BHSEhGbE0/view?usp=drivesdk

## Description
- [Build a text input box (contenteditable div) using ReactJS library Draft.js](https://facebook.github.io/draft-js/) that behaves like a normal text input box except it autocompletes the following:

- hashtags (#)
- @-signs
- related ideas subsequent to the <> string

For now, make up fake data to populate the list of suggested hashtags, @-signs.
- Element on the list can be chosen through arrow keys and pressing enter or tab
- [[Post it on a server and email it to careers@ideapad.io](mailto:careers@ideapad.io) and jacob@ideapad.io](mailto:jacob@ideapad.io)

Warning: it’s tricky to get this working in a way that is actually bug free and seamless to use. That’s what we are really evaluating this on, above all.  As far as we know, all approaches using off-the-shelf libraries end up with subtle bugs,  so we recommend doing it from scratch with DraftJS.

Please cite your sources if you use external libraries or copy/modify any existing code.

## Spec Details
The autocomplete editor should be capable of taking user's keyboard and mouse input
to allow its text content to be edited freely. At the same time the editor should
be capable of going through an autocomplete process described in more details below.
When the user finishes inputting a specific string an autocomplete process should
be started. There are two strings that trigger it:
the autocomplete process:

  - `#` (autocomplete process triggered with it should be called 'hashtag')
  - `@` (autocomplete process triggered with it should be called 'person')
  - `<>` (autocomplete process triggered with it should be called 'relation')

The string of all subsequently entered characters directly to the right of the trigger characters is called a "match string".

To be more precise in the definition of the “match string” — at any point in time after the autocomplete process was started and before is was finished, the “match string” is defined to be the longest continuous substring of the text following the trigger characters, containing only characters that were added into the text after the autocomplete process was started.

If the above definition of the “match string” proves to be too difficult to implement use the following one: The “match string”  is the continuous substring of the text extending from the right of the trigger characters to the caret (if caret is to the right of the trigger characters and to the left of any other “match string” or “autocompleted entry”, otherwise “match string” is empty)

When the autocomplete process is ongoing a list of options should be displayed.
Such list should be placed below the text that triggered its appearance.
The content of the list should be dynamically updated in response to the user's input.
Every option displayed in the list should be a string a prefix of which is the
"match string".

Based on what type of autocomplete process was triggered the pool of options to match
should be different. For now you can hardcode some example data.
In the list of options one should be highlighted. Responding to the up arrow and
down arrow presses, the highlighted option should change accordingly.
The autocomplete process should be finished when the user presses ENTER or TAB. Then the
editor should display an "autocompleted entry" instead of the “match string”. An "autocompleted
entry" should be a different color text and it should not be editable (it can be removed
with backspace or delete).

The value of the autocompleted entry should be equal to the highlighted option,
or if no option was present the "match string".
For the 'hashtag' process the autocomplete should also be finished when a user presses space.

Warning: With this spec there could be multiple autocomplete processes happening at the same time.