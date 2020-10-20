#include <stdio.h>
#include <string.h>

void make_new_name(char *new_name, char *original_name){
    char new_array[4] = "new-";
    for (int i = 0; i < 5; i++){
        new_name[i] = new_array[i];
    }
    for (int i = 0; i < 15; i++){
        new_name[i+4] = original_name[i];
    }
}

int length_of_password(char *password){
    int index = 0;
    int count = 0;
    char c = password[index];
    while (c != '\0'){
        count = count + 1;
        index = index + 1;
        c = password[index];
    }
    return count;
}

int is_alpha(char c){
    char alphabet[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    for(int i = 0; i < 26*2; i ++){
        if (c == alphabet[i]){
            return 1;
        }
    }
    return 0;
}

int is_digit(char c){
    char digit[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'};
    for(int i = 0; i < 10; i ++){
        if (c == digit[i]){
            return 1;
        }
    }
    return 0;
}

int is_valid_password(char *password){
    int len = length_of_password(password);
    int check;
    int alphaCheck = 0;
    int digitCheck = 0;
    for (int i = 0; i < len; i ++){
        int alpha = is_alpha(password[i]);
        if (alpha == 1){
            alphaCheck = 1;
            break;
        }
    }
    for (int i = 0; i < len; i ++){
        int digit = is_digit(password[i]);
        if (digit == 1){
            digitCheck = 1;
            break;
        }
    }

    if (len < 8){
        printf("The password needs to have at least 8 characters.\n");
        check = 0;
    }

    if (alphaCheck == 0){
        printf("The password needs to contain at least 1 alphabetical character.\n");
        check = 0;
    }

    if (digitCheck == 0){
        printf("The password needs to contain at least 1 digit.\n");
        check = 0;
    }

    if (alphaCheck == 1 && digitCheck == 1 && len >= 8){
        check = 1;
    }

    return check;

}

void perform_XOR(char *input_filename, char *output_filename, char *password){
    FILE *file, *newFile;
    int blockSize = length_of_password(password);
    char block[blockSize];
    int i, numBytes;
    file = fopen(input_filename, "rb");
    newFile = fopen(output_filename, "wb");
    do{
        numBytes = fread(block, 1, blockSize, file);
        for (i=0; i<numBytes; i++){
            block[i] = block[i]^password[i];
        }
    fwrite(block, 1, numBytes, newFile);
    } while(numBytes == blockSize);
    fclose(newFile); fclose(file);
}
void print_first_five(char *filename){
    FILE *file;
    int byte, curr, count = 0;
    int i, j;
    long int remainder, quotitent;
    file = fopen(filename, "rb");
    char hex[4];

    while(count < 5){
        count = count + 1;
        byte = getc(file);
        i=1;
        j=0;

        //converting to hex
        quotitent = byte;
        while(quotitent != 0){
            curr = quotitent % 16;
            if (curr < 10){
                curr = curr + 48;
            }
            else{
                curr = curr + 55;
            }
            hex[i++] = curr;
            quotitent = quotitent / 16;
        }
        for (j = i -1 ;j> 0;j--)
	        printf("%c",hex[j]);
        printf("\n");

    }
   fclose(file);
}

char conver_to_hex(int decimal){
    char hex[1];
    long quotient, remainder;
    int i = 0;

}

int main(int argc, char *argv[]) {
    char new_name[19];
    make_new_name(new_name, argv[1]);

    //print new name
    printf("New filename = %s\n", new_name);

    //check len of password
    int length = length_of_password(argv[2]);
    printf("Password length = %d\n", length);

    //check valid passowrd
    int valid_check = is_valid_password(argv[2]);

    //perform XOR
    if (valid_check == 1){
        perform_XOR(argv[1], new_name, argv[2]);
    }

    //print first five
    print_first_five(new_name);




}

