import psutil


class ProcessMemory:
    cores: int
    logical_cores: int
    max_freq: float
    min_freq: float

    user: float | None
    system: float | None
    idle: float | None
    nice: float | None
    iowait: float | None

    user_percent: float | None
    system_percent: float | None
    idle_percent: float | None
    nice_percent: float | None
    iowait_percent: float | None

    usage: float | None
    one_min_avg: float | None
    five_min_avg: float | None
    fifteen_min_avg: float | None
    current_freq: float | None

    def __init__(self):
        psutil.cpu_times()
        psutil.cpu_percent()

        self.logical_cores = psutil.cpu_count() or 0
        self.cores = psutil.cpu_count(logical=False) or 0

        freq = psutil.cpu_freq()
        self.min_freq = freq.min
        self.max_freq = freq.max

    def update(self):
        times = psutil.cpu_times()
        self.user = times.user
        self.system = times.system
        self.idle = times.idle
        self.nice = times.nice
        self.iowait = times.iowait

        times_percent = psutil.cpu_times_percent()
        self.user_percent = times_percent.user
        self.system_percent = times_percent.system
        self.idle_percent = times_percent.idle
        self.nice_percent = times_percent.nice
        self.iowait_percent = times_percent.iowait

        self.usage = psutil.cpu_percent()

        freq = psutil.cpu_freq()
        self.current_freq = freq.current

        [
            self.one_min_avg,
            self.five_min_avg,
            self.fifteen_min_avg,
        ] = [x / float(self.logical_cores) * 100 for x in psutil.getloadavg()]

    def __str__(self) -> str:
        return (
            f"cores: {self.cores}; logical_cores: {self.logical_cores}; max_freq: {self.max_freq}; min_freq: {self.min_freq};\n"
            + f"user: {self.user}; system: {self.system}; idle: {self.idle}; nice: {self.nice}; iowait: {self.iowait};\n"
            + f"user_percent: {self.user_percent}; system_percent: {self.system_percent}; idle_percent: {self.idle_percent}; nice_percent: {self.nice_percent}; iowait_percent: {self.iowait_percent};\n"
            + f"usage: {self.usage}; one_min_avg: {self.one_min_avg}; five_min_avg: {self.five_min_avg}; fifteen_min_avg: {self.fifteen_min_avg}; current_freq: {self.current_freq};"
        )
