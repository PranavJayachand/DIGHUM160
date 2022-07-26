from rich.progress import (BarColumn, MofNCompleteColumn, Progress,
                           SpinnerColumn, TaskProgressColumn, TextColumn,
                           TimeElapsedColumn)


class ProgressDisplay:
    """Implement a progress bar with rich over any iterable. Needs to be a class
    rather than a generator function since a lot of dependencies iterate over the iterables
    multiple times"
    """

    def __init__(self, iterable, length=None, iter_count=1, msg=None):
        self.iterable = iterable
        self.length = length
        self.msg = msg
        self.iter_count = iter_count
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn(
                "[bold blue][progress.description]{task.description}"
                if self.msg
                else ""
            ),
            BarColumn(),
            TaskProgressColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
        )
        self.task_id = self.progress.add_task(self.msg, total=len(self) * iter_count)
        self.progress.start()
        self.cur_iter = 0

    def __iter__(self):
        yield from self.display_progress()
        self.cur_iter += 1
        if self.cur_iter == self.iter_count:
            self.progress.stop()

    def __len__(self):
        return self.length if self.length else len(self.iterable)

    def display_progress(self):
        """
        Displays a progress bar using Rich for an iterable of a given length.
        """
        for i in self.iterable:
            yield i
            self.progress.update(self.task_id, advance=1)
        self.progress.update(self.task_id, refresh=True)
