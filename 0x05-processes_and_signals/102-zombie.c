#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * main - program that creates 5 zombie processes.
 * Return: 0 for success
 * Description: program that creates 5 zombie processes.
 *
 */
int main(void)
{
	int a;
	pid_t pid;

	a = 0;
	while (a < 5)
	{
		pid = fork();
		if (pid)
        {
			printf("Zombie process created, PID: %a\n", pid);
        }
		else
        {
			exit(0);
        }
		a++;
	}
	sleep(100);
	return (0);
}
