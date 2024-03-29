const circularProgressBar = document.querySelector('#circularProgressBar');
const circularProgressBarNumber = document.querySelector('#circularProgressBar .progress-value');
const buttonTypePomodoro = document.querySelector('#buttonTypePomodoro');
const buttonTypeShortBreak = document.querySelector('#buttonTypeShortBreak');

const pomodoroTimerInSeconds = 1500; // 60 segundos * 25 minutos
const shortBreakTimerInSeconds = 300;
const TIMER_TYPE_POMODORO = 'POMODORO';
const TIMER_TYPE_SHORT_BREAK = 'SHORTBREAK';

let progressInterval;
let pomodoroType = TIMER_TYPE_POMODORO;
let timerValue = pomodoroTimerInSeconds;
let multiplierFactor = 360 / timerValue;

function formatNumberInStringMinute(number) {
    const minutes = Math.trunc(number / 60).toString().padStart(2, '0');
    const seconds = (number % 60).toString().padStart(2, '0');
    return `${minutes}:${seconds}`;
}

const startTimer = () => {
    progressInterval = setInterval(() => {
        timerValue--;
        setInfoCircularProgressBar();
    }, 1000);
};

const stopTimer = () => clearInterval(progressInterval);

const resetTimer = () => {
    clearInterval(progressInterval);
    timerValue = (pomodoroType === TIMER_TYPE_POMODORO)
        ? pomodoroTimerInSeconds
        : shortBreakTimerInSeconds;
    multiplierFactor = 360 / timerValue;
    setInfoCircularProgressBar();
    // audio.stop(); // Seu objeto de áudio pode precisar de ajustes aqui
};

function setInfoCircularProgressBar() {
    if (timerValue < 0) {
        stopTimer();
        // audio.play(); // Tocar som quando o temporizador chegar a zero
        timerValue = 0; // Garante que o timerValue não seja negativo
    }

    circularProgressBarNumber.textContent = formatNumberInStringMinute(timerValue);
    circularProgressBar.style.background = `conic-gradient(var(--blue) ${(pomodoroTimerInSeconds - timerValue) * multiplierFactor}deg, var(--purple) 0deg)`;
}

const setPomodoroType = (type) => {
    pomodoroType = type;

    if (type === TIMER_TYPE_POMODORO) {
        buttonTypeShortBreak.classList.remove("active");
        buttonTypePomodoro.classList.add("active");
    } else {
        buttonTypePomodoro.classList.remove("active");
        buttonTypeShortBreak.classList.add("active");
    }

    resetTimer();
};
