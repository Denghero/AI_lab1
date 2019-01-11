{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to Artificial Intelligence for Non Computing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Practical 4 (weeks 7 - 8)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Theory Questions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1\\.Symbolize the following proposition and discuss the truth.\n",
    "1. Everyone has black hair.\n",
    "2. Some people boarded the moon.\n",
    "3. No one has boarded Jupiter\n",
    "4. Students studying in the US are not necessarily Asians."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_your answer here..._\n",
    "∀xBH(x)    false\n",
    "∃xM(x)     true\n",
    "￢∃xJ(x)   true\n",
    "∃x￢A(x)   true\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2\\.Judge the following formula, which is tautology? What is the contradiction?\n",
    "1. ∀xF(x)⇒(∃x∃yG(x,y))⇒∀xF(x))\n",
    "2. ￢( ∀xF(x)⇒∃yG(y))∧∃yG(y)\n",
    "3. ∀x(F(x)⇒G(y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_your answer here..._ \n",
    "1.tautology\n",
    "2.contradiction\n",
    "3.contradiction\n",
    "\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3\\.Which of the following are correct?\n",
    "1. False |=True.\n",
    "2. (A ∧ B) |= (A ⇔ B).\n",
    "3. (A ∧ B) ⇒ C |= (A ⇒ C) ∨ (B ⇒ C).\n",
    "4. (A ∨ B) ∧ (￢C ∨￢D ∨ E) |= (A ∨ B).\n",
    "5. (A ∨ B) ∧ (￢C ∨￢D ∨ E) |= (A ∨ B) ∧ (￢D ∨ E)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_your answer here..._ \n",
    "1,2,3,4 are ture.\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4\\.Conjunctive normal form.link:https://baike.baidu.com/item/%E5%90%88%E5%8F%96%E8%8C%83%E5%BC%8F/2459360\n",
    "1. Obtaining conjunctive paradigm: P∧(Q⇒R)⇒S\n",
    "#### Basic steps to find a conjunctive normal form.\n",
    "1. Cut redundant connectives，Reserved {∨，∧，￢}\n",
    "2. Move or remove the negation ~\n",
    "3. distribution rates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_your answer here..._ \n",
    "P∧(Q⇒R)⇒S\n",
    "= P∧(￢Q∨R)⇒S\n",
    "=￢(P∧(￢Q∨R))∨S\n",
    "=￢P∨(Q∧￢R)∨S\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5\\.Arithmetic assertions can be written in first-order logic with the predicate symbol <,the function symbols + and ×, and the constant symbols 0 and 1. Additional   predicates can also be defined with biconditionals.(Chapter 8.20)\n",
    "1. Represent the property “x is an even number.”\n",
    "2. Represent the property “x is prime.”\n",
    "3. Goldbach’s conjecture is the conjecture (unproven as yet) that every even number is equal to the sum of two primes. Represent this conjecture as a logical sentence.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "_your answer here..._ \n",
    "1.∀xEven(x) ⇔ ∃y(x=y+y).\n",
    "2.∀xPrime(x) ⇔ ￢∃y,z(x=y×z)\n",
    "3.∀x(∀y∀z(Even(x)⇒SumPrime(y,z)))\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Programming Excercises"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Take the multiagent folder from assignment 2 and copy into a new directory for this practical. We will implement a version of minimax for Ghost Agents to make very smart ghosts.\n",
    "\n",
    "First look at the file ghostAgents.py. Try to play classic pacman against the directional ghost and the random ghost. Use the following option:\n",
    "\n",
    "\n",
    "-g TYPE, --ghosts=TYPE\n",
    "                        the ghost agent TYPE in the ghostAgents module to use\n",
    "                        [Default: RandomGhost]\n",
    "\n",
    "Now implement a new ghost agent called MinimaxGhost. You will need to create a new class and methods in the file ghostAgent (you can ask the tutor if you need help to create the method stub).\n",
    "\n",
    "\n",
    "This will involve implementing the following methods:\n",
    "\n",
    "---\n",
    "<code>\n",
    "class MinmaxGhost ( GhostAgent ):\n",
    "\n",
    "    def __init__( self, index, ...):\n",
    "\t\t...\n",
    "\t\t\n",
    "\t\t\n",
    "\tdef getAction(self, state):\n",
    "\t\t...\n",
    "\n",
    "\tdef getDistribution(self, state):\n",
    "\t\t...\n",
    "</code>\n",
    "---\t\t\n",
    "\n",
    "\n",
    "To test whether or not you have implemented correctly you will need to compare the behaviour of your new ghost agent with the random ghost agent. This has to be done over multiple tests (e.g. 10 runs).\n",
    "\n",
    "- You can turn off the graphical display to use options -t or -q\n",
    "- You can perform multiple runs (e.g. 10) by setting the -numGames=10\n",
    "- You can fix the random seed as well.\n",
    "\n",
    "Try to use different layouts to test. A simple layout might be good for testing initially as you are developing your algorithm. New layout files can be created in the layout directory (must be saved with end of file name \".lay\"). For example:\n",
    "smallClassic.lay\n",
    "<code>\n",
    "%%%%%%%%%%%%%%%%%%%%\n",
    "%......%G  G%......%\n",
    "%.%%...%%  %%...%%.%\n",
    "%.%o.%........%.o%.%\n",
    "%.%%.%.%%%%%%.%.%%.%\n",
    "%........P.........%\n",
    "%%%%%%%%%%%%%%%%%%%%\n",
    "</code>\n",
    "newLayout.lay:\n",
    "<code>\n",
    "%%%%%%%\n",
    "% %G% %\n",
    "% % % %\n",
    "% % % %\n",
    "%%%P%%%\n",
    "%     %\n",
    "% %%% %\n",
    "% % % %\n",
    "% % % %\n",
    "% %%% %\n",
    "%  .  %\n",
    "%%%G%%%\n",
    "%%%%%%%\n",
    "</code>\n",
    "\n",
    "Please try to make some different layouts such as in this example,(the ghosts are marked by G, walls by % and pacman starting position by P,\".\" for pellet)\n",
    "<div style=\"float:center;\" ><img src=\"img/p2.png\" width=\"200\" height=\"50\" ></div>\n",
    "\n",
    "---\n",
    "\n",
    "2\\. \n",
    "In this question we will test the new ghostAgent with different pacman agents. In your assignment you were asked to complete a Minimax pacman a version of Expectimax for pacman was provided. If you have not completed the assignment just use the provided expectimax version.\n",
    "\n",
    "We will perform some experiments to compare the performance of pacman against different types of ghost agent:\n",
    "- a random (not smart) ghost vs a pacman that assumes optimal play from ghosts (ie minimax pacman).\n",
    "- a smart (minmax) ghost vs a pacman that assumes optimal play from ghosts\n",
    "- random ghosts vs pacman that assumes ghosts may not always do an optimal move\n",
    "- smart (minimax) ghosts vs pacman that assumes that ghosts may do suboptimal moves.\n",
    "\n",
    "\n",
    "This will result in a table similar to the following:\n",
    "\n",
    "<div style=\"float:center;\" ><img src=\"img/p1.png\" width=\"400\" height=\"300\" ></div>\n",
    "\n",
    "\n",
    "   \n",
    "3\\.\n",
    "Describe the performance (in terms of the distribution) of Pacman in each case.\n",
    "\n",
    "In which cases is the Pacman agent implementing the correct assumption of the ghosts behaviour?\n",
    "\n",
    "\n",
    "4\\. Describe why the ghosts seem as if they are cooperating when using minimax even though they are not sharing information with each other.\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
