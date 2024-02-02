|                       | **Term**             | **Definition**                                                           | **Note** |
|-----------------------|----------------------|--------------------------------------------------------------------------|----------|
| **Classes**           |                      |                                                                          |          |
|                       | `Thing`              | Any physical or conceptual entity.                                       |          |
|                       | `WorkflowExecution`  | An event that executes a workflow.                                       |          |
|                       | `Workflow`           | An ordered sequence of steps.                                            |          |
|                       | `Step`               | A unit of a workflow.                                                    |          |
|                       | `AssessmentActivity` | An activity that executes a risk assessment workflow step.               |          |
|                       | `Agent`              | An individual or a group of individuals.                                 |          |
|                       | `TimeInterval`       | A period of time.                                                        |          |
|                       | `Document`           | An informational object.                                                 |          |
|                       | `Duration`           | The duration of a step.                                                  |          |
| **Object properties** |                      |                                                                          |          |
|                       | `executes`           | A relationship between a workflow execution and a workflow.              |          |
|                       | `involvesActivity`   | A relationship between a workflow execution and a assessment activity.   |          |
|                       | `hasStep`            | A relationship between a workflow and a step.                            |          |
|                       | `hasFirstStep`       | A relationship between a workflow and its first step.                    |          |
|                       | `hasNextStep`        | A relationship between a step and the step that comes immediately after. |          |
|                       | `hasDuration`        | A relationship between a step and a duration.                            |          |
|                       | `isExecutedIn`       | A relationship between a step and a assessment activity.                 |          |
|                       | `isDocumentedBy`     | A relationship between a assessment activity and a document.             |          |
|                       | `atTime`             | A relationship between a assessment activity and a time interval.        |          |
|                       | `targets`            | A relationship between a assessment activity and the thing it targets.   |          |
|                       | `assesses`           | A relationship between a assessment activity and the thing it assesses.  |          |
|                       | `hasParticipant`     | A relationship between a assessment activity and an agent.               |          |
| **Data properties**   |                      |                                                                          |          |
|                       | `hasStartDate`       | A property that assigns a starting date to a time interval.              |          |
|                       | `hasEndDate`         | A property that assigns a ending date to a time interval.                |          |
|                       | `hasDays`            | A property that assigns a number of days to a duration.                  |          |