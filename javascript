export type TaskListProps = {
  tasks: Task[];
  entityType: string;
  onUpdateHeaderContent: (headerLabel: string, headerState: string) => void;
};

export function TaskList({ tasks, entityType, onUpdateHeaderContent }: TaskListProps) {
  const [isOpen, setIsOpen] = useState(true);
  const numCompletedTasks =
    tasks.filter((task) => task.state === 'COMPLETE').length || 0;
  const numErrorTasks = tasks.filter(
    (task) => task.state === 'NEEDS_ATTENTION',
  ).length;
  const isOngoing = tasks.length === 1 && tasks[0].name === 'BOIR';
  const inProgress = numCompletedTasks !== tasks.length;

  const getState = () => {
    if (!!numErrorTasks) {
      return 'error';
    }
    if (!inProgress) {
      return 'complete';
    }
    if (isOngoing) {
      return 'ongoing';
    }
    return 'default';
  };

  const headerContent = getHeaderContent(
    entityType,
    numErrorTasks,
    tasks.length,
    numCompletedTasks,
  );

  const headerLabel = headerContent[getState()]?.label;

  useEffect(() => {
    onUpdateHeaderContent(headerLabel, getState());
  }, [headerLabel, getState(), onUpdateHeaderContent]);

  return (
    <div
      id="compliance-task-list"
      className="flex flex-col -mx-4 md:mx-0 md:rounded-lg bg-neutral-0 border border-neutral-100"
    >
      <Header
        entityType={entityType}
        totalTasks={tasks.length}
        completedTasks={numCompletedTasks}
        errorTasks={numErrorTasks}
        state={getState()}
        isOpen={isOpen}
        setIsOpen={setIsOpen}
      />

      <ol>
        {isOpen &&
          tasks.map((task, index) => (
            <li key={task.id}>
              <TaskItem
                task={task}
                headerLabel={headerLabel}
                headerState={getState()}
              />
              {index !== tasks.length - 1 && (
                <hr className="text-neutral-100" />
              )}
            </li>
          ))}
      </ol>
    </div>
  );
}