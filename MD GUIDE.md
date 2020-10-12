# MD guide
author : BruttherJOE

a simple guide on how to use md for text formatting.  
md is useful and comes naturally to me for making notes.

# This is a title

for titles, do # (yourtitlehere)  
for subtitles, do ## (yoursubtitlehere)  
for subsubtitles, do ### (yoursubsubtitlehere)  
and so on and so forth  
  
to force line return (new line), add ("  ") double spaces at the end of a line
## this is a subtitle

```
this is a body. use 
  ``` (yourtexthere) and then ``` again

```
for pictures, create a file called assets. stuff the pictures in. then you reference the picture from within the md file.

### Tables

You can create tables by assembling a list of words and dividing them with hyphens - (for the first row), and then separating each column with a pipe |:

```
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

```

would become:

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
<br/>
<br/>

### Inline code

`inline code`


```
`this inlines the code`
```
<br/>

### Pictures
make an ./assets folder. link your picture onto your .md file with this link location  
`![this_does_not_matter](./assets/<your_picture_name_and_extension.jpg>)`

Important info, remember that the link itself on github cannot have any spaces (use underscores `_` )
<br/>
<br/>
## HTML STUFF (Git supports this!)
### Subscript and superscript
This is some <sup>superscript</sup> text.

This is some <sub>subscript</sub> text.
```
This is some <sup>superscript</sup> text.

This is some <sub>subscript</sub> text.
```
<br/>

### Line breaks
```
<br/> : breaks a line
```
