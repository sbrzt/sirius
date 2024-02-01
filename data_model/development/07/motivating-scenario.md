# Iteration 07

## Name
Assessment workflow

## Description
A risk assessment workflow is characterized by a series of steps. Each step is a unit of the workflow executed in an assessment activity. An assessment activity is an action of the workflow that can consist in a context description activity, an identification activity, an analysis activity, an evaluation activity, a treatment activity, and so on. Each step is also characterized by a temporal duration. 

Each assessment activity targets something (such as a heritage asset), assesses something else (such as a value, a risk, etc.), and is characterized by a temporal interval, which in turn has a start and an end date.

A workflow is executed by a workflow execution event, which involves all the activities executed in each step that is part of the workflow.

## Example 01
The risk assessment process for a museum consists in a workflow composed of the following steps:
* context step (during a period of time of 10 days), executed in a context description activity done by Marta Cosentini between 2023-01-10 and 2023-01-20 that targets the museum, assesses something related to it, such as its perceived value, and is documented by a catalogue record about the museum;
* identify step (during a period of time of 30 days), executed in a identification activity done by Marta Cosentini between 2023-01-20 and 2023-02-20 that targets the museum, assesses something related to it, such as a risk of fires, and is documented by a historic record of the museum;
* analyze step (during a period of time of 5 days), executed in an analysis activity done by Marta Cosentini between 2023-02-20 and 2023-02-25 that targets the museum and assesses the risk of fires;
* evaluate step (during a period of time of 30 days), executed in an evaluation activity done by Marta Cosentini between 2023-02-25 and 2023-03-25 that targets the museum and assesses the risk of fires;
* treat step (during a period of time of 20 days), executed in a treatment activity done by Marta Cosentini between 2023-03-25 and 2023-04-15 that targets the museum and assesses the risk of fires.
