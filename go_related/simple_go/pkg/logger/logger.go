package logger

import (
	"log"
	"os"
)

var (
	infoLogger  *log.Logger
	warnLogger  *log.Logger
	errorLogger *log.Logger
)

func init() {
	infoLogger = log.New(os.Stdout, "[INFO] ", log.Ldate|log.Ltime|log.Lshortfile)
	warnLogger = log.New(os.Stdout, "[WARN] ", log.Ldate|log.Ltime|log.Lshortfile)
	errorLogger = log.New(os.Stderr, "[ERROR] ", log.Ldate|log.Ltime|log.Lshortfile)
}

func Info(msg string, v ...any) {
	infoLogger.Printf(msg, v...)
}

func Warn(msg string, v ...any) {
	warnLogger.Printf(msg, v...)
}

func Error(msg string, v ...any) {
	errorLogger.Printf(msg, v...)
}
