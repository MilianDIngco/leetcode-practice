#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* readline();
char* ltrim(char*);
char* rtrim(char*);
char** split_string(char*);


int parse_int(char*);


/*
 * Complete the 'roadsAndLibraries' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER c_lib
 *  3. INTEGER c_road
 *  4. 2D_INTEGER_ARRAY cities
 */


int MAXN = 125252;
int data[];
int n, m, cl, cr;



void compress(int value, int jawn[], int root) {
    if (jawn[value] == -1) {
        jawn[value] = root;
        return;
    } else {
        int temp = jawn[value];
        jawn[value] = root;
        compress(temp, jawn, root);
    }
}

// recursively finds the root of the tree containing the node containing value
int find(int value, int jawn[]) {
    if (jawn[value] == -1) {
        return value;
    } 
    return find(jawn[value], jawn);
}


// unites subtrees
void unite(int x, int y, int jawn[], int size[]) {
    // first do same component test
    int x1 = find(x, jawn);
    int y1 = find(y, jawn);
    if (x1 == y1) return;
    
    // if subtree containing x is smaller, attach to y
    if (size[x1] < size[y1]) {
            if (size[x1] > 1)
                compress(x, jawn, y1);
            else
                jawn[x1] = y1;
            size[y1] += size[x1];
        }
    
    // if subtree containing y is smaller, attach to x
    else {
        if (size[y1] > 1)
                compress(y, jawn, x1);
            else
                jawn[y1] = x1;
            size[x1] += size[y1];
    }
}


long roadsAndLibraries(int n, int c_lib, int c_road, int cities_rows, int cities_columns, int** cities) {
        if (c_lib < c_road)
            return c_lib * n;

        // run union find
        int size[n+1];
        size[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            size[i] = 1;
        }

        int cityTree[n+1];
        cityTree[0] = -2;
        for (int i = 1; i < n + 1; i++) {
            cityTree[i] = -1;
        }

        for (int i = 0; i < cities_rows; i++) {
            unite(cities[i][0], cities[i][1], cityTree, size);
        }

        long numLib = 0;
        long numRoads = 0;
        for (int i = 1; i < n+1; i++) {
            if (cityTree[i] == -1) {
                numLib++; // FOR EACH ROOT NODE, ADD A LIBRARY
                numRoads += (size[i] - 1); // FOR EACH ROOT NODE, FIND ITS SIZE - 1 AND /// ADD IT TO THE NUMBER OF ROADS // size of a tree = n - 1;
            }
        }

        long answer = (numLib * c_lib + numRoads * c_road);
        return answer;
    }




int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");


    int q = parse_int(ltrim(rtrim(readline())));


    for (int q_itr = 0; q_itr < q; q_itr++) {
        char** first_multiple_input = split_string(rtrim(readline()));


        int n = parse_int(*(first_multiple_input + 0));


        int m = parse_int(*(first_multiple_input + 1));


        int c_lib = parse_int(*(first_multiple_input + 2));


        int c_road = parse_int(*(first_multiple_input + 3));


        int** cities = malloc(m * sizeof(int*));


        for (int i = 0; i < m; i++) {
            *(cities + i) = malloc(2 * (sizeof(int)));


            char** cities_item_temp = split_string(rtrim(readline()));


            for (int j = 0; j < 2; j++) {
                int cities_item = parse_int(*(cities_item_temp + j));


                *(*(cities + i) + j) = cities_item;
            }
        }


        long result = roadsAndLibraries(n, c_lib, c_road, m, 2, cities);


        fprintf(fptr, "%ld\n", result);
    }


    fclose(fptr);


    return 0;
}


char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;


    char* data = malloc(alloc_length);


    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);


        if (!line) {
            break;
        }


        data_length += strlen(cursor);


        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }


        alloc_length <<= 1;


        data = realloc(data, alloc_length);


        if (!data) {
            data = '\0';


            break;
        }
    }


    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';


        data = realloc(data, data_length);


        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);


        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }


    return data;
}


char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }


    if (!*str) {
        return str;
    }


    while (*str != '\0' && isspace(*str)) {
        str++;
    }


    return str;
}


char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }


    if (!*str) {
        return str;
    }


    char* end = str + strlen(str) - 1;


    while (end >= str && isspace(*end)) {
        end--;
    }


    *(end + 1) = '\0';


    return str;
}


char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");


    int spaces = 0;


    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);


        if (!splits) {
            return splits;
        }


        splits[spaces - 1] = token;


        token = strtok(NULL, " ");
    }


    return splits;
}


int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);


    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }


    return value;
}



