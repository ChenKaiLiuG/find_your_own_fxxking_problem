// Under debugging
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *file;
    char filename[] = "找找自己問題.txt";
    char line[256]; 
    file = fopen(filename, "r");
    
    if (file == NULL) {
        perror("無法開啟檔案");
        return 1;
    }

    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }

    fclose(file);
    return 0;
}
