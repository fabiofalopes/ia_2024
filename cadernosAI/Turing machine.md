Based on the detailed notes from the Stanford Encyclopedia of Philosophy on Turing Machines, here is a simplified description of the algorithm of a Turing machine in steps:

1. **Initialisation**: The Turing machine starts in a predefined initial state with a tape that is infinite in one direction. The tape is divided into squares, each of which may contain a symbol from a finite alphabet. Initially, the tape contains a finite sequence of symbols (the input), and all other squares are blank.

2. **Reading**: The machine scans one square of the tape at a time. This square could either contain a symbol from its alphabet or be blank.

3. **Transition**: Based on the current state of the machine and the symbol it is scanning (together referred to as the "current configuration"), the machine consults its set of rules (or program) to decide on the action to take. These rules are defined as quintuples or quadruples, specifying the current state, the symbol being read, the symbol to write, the direction to move in (left or right), and the next state of the machine.

4. **Action**: According to the rule selected in the previous step, the machine performs three types of actions:
   - **Print**: Replace the symbol in the current square with a new symbol (which could be the same as the old one or different, including a blank symbol).
   - **Move**: Move the tape one square to the left or right.
   - **Change State**: Transition to a new state, which could include a special halting state to end the computation.

5. **Loop**: Repeat steps 2 through 4 until the machine reaches a halting state. At this point, the sequence of symbols left on the tape is considered the output of the computation.

6. **Halting**: The machine stops its computation. The content of the tape can be interpreted as the result of the computation process.

It's important to note that the Turing machine is a theoretical model that captures the essence of algorithmic computation. It operates under the assumptions of having potentially infinite memory (the tape) and time to perform the computation. The simplicity and power of this model lie in its ability to simulate any algorithm, thereby serving as a foundational concept in the theory of computation and the formulation of the Church-Turing thesis.