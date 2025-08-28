/*
 * syscalls.c
 *
 *  Created on: Apr 14, 2025
 *      Author: Leonard Lochte-Holtgreven
 */

#include <sys/stat.h>

int _read(int file, char *ptr, int len) {
    return -1;
}
//int _write(int file, char *ptr, int len) {
//    return -1;
//}
int _close(int file) {
    return -1;
}
int _fstat(int file, struct stat *st) {
    return -1;
}
int _isatty(int file) {
    return 0;
}
int _lseek(int file, int ptr, int dir) {
    return 0;
}
int _kill(int pid, int sig) {
    return -1;
}
int _getpid(void) {
    return 1;
}
