## Part 3: Visualization

For the results from Part 2, we did simple line plots to track the emotions of the main characters across the chapters.
We also overlapped the line plots and compared these results with the content of the book.
Additionally, we created box plots which allow us more insight into outliers and the distribution of data in detail.
For the results from Part 0, we tracked the occurences of positive and negative emotions across the entire book. In this part we had to change the code a little bit to make it easier for us to plot the data. The change we made is that the code sorts the sentiments already into positive and negative sentiments.
This way we could just get the length of the list of positive and negative sentiments and plot them.
To further investigate the development of the sentiments, we checked our JSON files from part 0 and created a bar graph which tracks the 5 most commonly named sentiment values.
As a last visual, we tracked the co-occurence of our 4 main characters' names.

## Part 4: Reflection and Discussion

Our learning experience, project insights, and real-world applicability.

a. Learning and Challenges

* Comparing the results of grep and the more in-depth NLP analysis, what are the key insights?

> Grep was a quick and simple way to identify patterns and occurences in our books. It was very effective when kept simple: In part 0, we found a lot of occurences, but the more context we had to add (to capture entire sentences with the main character names and sentiments), the more matches probably escaped. We got to a reasonable number in the end, but it would have taken a lot of work to find all the sentences with main characters in them.

> Grep really reached its limits when characters had multiple aliases, which is often the case in Dracula (characters have first names, last names and sometimes titles). Here, NLP allowed us a more nuanced understanding of the text, particularly spaCy's NE. The possibility to capture variations and aliases of names and cluster them is very valuable in literary analysis, but also in texts from everyday life.

> For sentiment analysis, NLP tools are very important and surprisingly advanced. With a simple grep, we could only identify the presence of specific sentiment-related words but not score them or analyze their context. By evaluating different tools for sentiment analysis, we could very quickly get to a more detailed understanding of the emotional tone associated with each character.

* You were asked to visualise both methods. How do they differ?
> As discussed in part 3, our results can not directly be compared. For part 2, we have JSON files which contain main character names and their sentiment values across chapters. For part 0, we produced 2 JSON files per chapter: one for the entities and one for the sentiments, as instructed in the PDF.

> We visualized the results for Dracula and the visuals for our methods don't contradict each other. The visualization of part 0 shows a surprising strong presence of positive words for a horror novel, which fits with the emotional plots of the characters (mostly on the positive side). However, the visuals for part 2 tell a more detailed story between the characters. While some experience mostly positive emotions (Jonathan), others are all over the place (Lucy).

> The more advanced methods basically allowed us to further explore and explain the results of the basic grep in part 0.

* Summarize key learnings, focusing on technical skills and literary insights.

> We developed our skills with grep for a basic text pattern analysis.
> We learned how to use NLP tools to analyze text, including named entity recognition and sentiment analysis.
> We explored implementing clustering techniques for entity resolution.
> We creatively tried out different visualization techniques in python.
> We also learned how to use command line arguments to make our code more dynamic.
> We also learned a lot about the os library which will be very useful in the future.
> We gained more insight into Dracula than we ever expected!

* Briefly discuss major challenges and how you addressed them, particularly moving from basic grep searches to advanced NLP.

> Grepping was a bit of a pain because we had to decided what we wanted to grep for and this was not always easy. For example in part 0 we had to grep for the names of the characters and the sentiment words and then if we realized that there is another name or word we wanted to grep we had to change the code and rerun everything again. When starting to code the rest where we had to iterate through hole folders and set paths etc. we had to read into the os package documentation, look at examples and also ask chatGPT for help because certain things done with the os package were not very intuitive. We then had to also look up how to use the packages used for graphic which wasnt as hard but still took some time.

> We also learned that getting to the result you want is a cyclic exercise: you first need to get your code to run, then refine it, which may have an impact on earlier functions which you then need to refine as well. For some parts, this meant rerunning it a lot - which tended to take a lot of time if, for example, it had to go over all the chapters of the book.

b. Analysis Insights and Real-World Applicability

* Describe significant insights from the book analysis and how advanced NLP tools enhanced your initial grep findings.

> When using NLP tools we didnt have to think as much what we want to grep for. We could just use the tools to find the sentiment of the sentences and then just filter out the sentences that contain the names of the characters we are interested in. This way we could get more accurate results. Also we could get more context about the sentences that contain the names of the characters we are interested in which helped us to understand the emotions of the characters better and in which situations they were in.

* Reflect on how these techniques and insights could apply in real-world contexts, like social media analysis or other literary works.

> We could imagine that these techniques could be used to analyze the emotions of people on social media. For example we could use the same techniques to analyze the emotions of people on twitter. We could then use the results to see how people feel about a certain topic. For example we could analyze the emotions of people on twitter about the corona virus and see how people feel about it. We could then use the results to see if people are more positive or negative about the corona virus and then use the results to make decisions about the way we handle corona virus related topics/posts.

> In a literary context, these tools could be useful in exploring how sentiment expressions change between genres or over time. We could research if Dracula an unusually romantic horror book for its time or does if it fits with other books of its time. Or we could look at if horror books have become more or less emotional since 1897.

> As another real-life example, sentiment analysis could be useful to go over reviews for books, movies or even brands. They could provide insight into how much a piece of media resonated with its audience, if it provoked strong opinions and how positive or negative these are.

## --- Feedback ---

The project was very interesting overall. However the instructions were not given in a  clear way and this led to quite a lot of frustration. For example, in part 1 and 2, we tried to apply our code to all 3 books and only found out quite late that we could have picked just 1. Also, the comparison between the results of part 0 and part 2 in part 3 did not seem sensible because the instructions for creating the results for part 0 were too ambigious. Of course we came up with something to compare, but it really did not feel very worthwile. If we'd been instructed in part 0 to grep the names and sentiments together, we could have avoided this.
