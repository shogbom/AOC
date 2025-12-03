#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

int main() {
    long long sum = 0;
    int status = 1;
    std::ifstream f("list");
    std::string line;
    while (std::getline(f, line)) {
        std::cout << status << "\n";
        status++;
        long long maxv = 0;
        int n = line.size();
        for (int a = 0; a < n; a++)
            for (int b = a + 1; b < n; b++)
                for (int c = b + 1; c < n; c++)
                    for (int d = c + 1; d < n; d++)
                        for (int e = d + 1; e < n; e++)
                            for (int f2 = e + 1; f2 < n; f2++)
                                for (int g = f2 + 1; g < n; g++)
                                    for (int h = g + 1; h < n; h++)
                                        for (int i = h + 1; i < n; i++)
                                            for (int j = i + 1; j < n; j++)
                                                for (int k = j + 1; k < n; k++)
                                                    for (int l = k + 1; l < n; l++) {
                                                        long long val =
                                                            (line[a] - '0') * (long long)std::pow(10, 11) +
                                                            (line[b] - '0') * (long long)std::pow(10, 10) +
                                                            (line[c] - '0') * (long long)std::pow(10, 9)  +
                                                            (line[d] - '0') * (long long)std::pow(10, 8)  +
                                                            (line[e] - '0') * (long long)std::pow(10, 7)  +
                                                            (line[f2] - '0') * (long long)std::pow(10, 6) +
                                                            (line[g] - '0') * (long long)std::pow(10, 5)  +
                                                            (line[h] - '0') * (long long)std::pow(10, 4)  +
                                                            (line[i] - '0') * (long long)std::pow(10, 3)  +
                                                            (line[j] - '0') * (long long)std::pow(10, 2)  +
                                                            (line[k] - '0') * 10LL +
                                                            (line[l] - '0');

                                                        if (val > maxv)
                                                            maxv = val;
                                                        }

                                                        sum += maxv;
                                                    }
    std::cout << sum << "\n";
    return 0;
}
