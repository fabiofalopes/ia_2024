## Format 
```
Maquina de turing e Introdução a redes neuronais 

Tabela
Fazer fita

1.Tabela
	1.1. Faz a fita
	1.2. Diagrama de transição de estado (hexágonos)
2.Faz uma rede neuronal 
```

___

**Turing machine consists of the following components:**

1. An infinite storage “tape” partitioned into cells
2. An alphabet of symbols
3. A read/write head
4. The machine state
5. A set of instructions (program), stored in a 2D table

--- 

**Instruction format is:**
(_current state_, _current symbol_, _next symbol_, _next state_, _direction_)

```
The TM interprets instruction (**i**, **j**, **k**, **s**, **d**) as:

IF current state is **i** AND current symbol is **j**

THEN

   Write symbol **k** on tape (replacing **j**)

   Set machine state to **s**

   Move read/write head one cell in direction **d**

ENDIF

```


**Additional TM Rules:**
1.  finite number of symbols on the tape (blanks on both sides).
2.  initial configuration of TM is:
	- finite input contained on tape
	- the R/W head is positioned at the first (leftmost) input symbol,
	- initial state is specified (usually 0 or 1).
3.  If no instruction for current state and input symbol exists, the machine halts.
4.  The output is what remains on the tape when the machine halts