# MIS203 - Basic Programming

İzmir Demokrasi University – Management Information Systems

Course repository for in-class assignments.

## Assignments

* [Bug Assignment](bug-assignment/) – fix the bugs in your own program and send a pull request.

## Week 02

- **AI Tool Used:** OpenAI Codex
- **Prompt Used:** "bir de bu ödevi yapmam lazım" (I attached the assignment screenshots with this prompt.)
- **What did you change?** With AI assistance, I added `week02/grade_calculator.py` to enter student names and scores repeatedly, assign letter grades, and report the student count and average. Invalid scores are skipped and are not included in the totals.
- **What does break do in your program?** When I enter `q`, `break` exits the loop so the program can print the final summary.

## Week 03

- **AI Tool Used:** OpenAI Codex
- **Prompt Used:** "ödevi yapar mısınm" (I attached the GitHub 3 assignment screenshots with this prompt.)
- **What did you change?** With AI assistance, I added `week03/ticket_office.py` to validate customer information, apply one ticket discount, and print sales totals. The program accepts upper- or lowercase answers for the quit command, day, and student status.
- **Tests:**
  1. Input: the six customers from the example (Ali, Zeynep, Can, Elif, Deniz, and Mert). Result: `Tickets sold: 6`, `Total revenue: 810.00 TRY`, `Average price: 135.00 TRY`, and `Free tickets: 1`.
  2. Input: `Ece`, age `6`, `weekday`, student `yes`. Result: `Ece: 120.00 TRY (Child)`. This tests the boundary where the Child discount begins.
  3. Input: `Deniz`, age `121`, followed by `q`. Result: `Invalid age.` and then `No tickets sold.`
- **Why does the order of the rules matter?** The program stops checking after the first matching rule, so the more specific age rules must come before the Student rule. For example, a 10-year-old student must receive the Child discount instead of the Student discount.
