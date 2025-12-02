# What Did I Do?
Welcome to Part E. I (Dorian) was tasked with trying to poke holes in our approximate solution and then adjusting the code accordingly. I used Microsoft Copilot heavily during this task.

I began by finding weaknesses with our approximate solution, which I will call v1. This version didn't implement any randomness, and is dependent on the starting node. It also tries to remove crossing edges via its 2_opt function, which only looks at local edge swaps and changes the actual path, which could cause bugs.

These problems were fixed in v2. Now, multiple starting positions are compared and the best is accepted. Additionally, randomness was implemented, and a function was created to ensure consistently formatted output. V2 was able to provide the optimal answer to the problem that stumped v1, but found a new problem it could only provide the optimal answer for semi-reliably (Query 7).

To solve this, I created v2.5. This had a for loop around the main work of nearest neighbor -> two_opt -> reformat. My theory was that if I ran the process enough times, it would guarantee the result within 1 run of the actual program itself. My experiments are detailed in Appendix A, but to make a long story short, it didn't affect the odds. Either I made an error in actually implementing the theory, or the theory didn't work.

So I went back to analyze the flaws with v2. Turns out there was a small bug with the formatting. Beyond that, however, it also utilized very little randomness which means it explores few options. With some changes, v3 was made, which features a small amount of randomness in 2_opt and more randomness in nearest_neighbor.

V3 did brilliant work with Query 9 as a sample input, getting near the answer 86% of the time (full data in the Query 10, 11, 12 section). However, it did rather poorly on Query 7. v2 would find a path of length 108 around 76% of the time, and the optimal answer of 11 around 20% of the time. V3 would find an answer >= 108 57% of the time, and <= 13 43% of the time. Note the weird ranges -- v3 can fluctuate and create a path as long as 207 and as short as 11. Overall, the odds of getting something near the answer are higher, but the odds for the actual answer itself is lower.

Clearly, v3 needed to be amended. The main steps of nearest neighbor -> two_opt -> reformat were put in a for loop that runs for 50 times by default. Sound familiar? Well it should -- this is v2.5 but actually functional due to the new randomness and changes. Thus, 3.5 was born, which I have dubbed Zenith.
