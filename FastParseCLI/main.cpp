#include "FileProcessor.hpp"
#include <iostream>
#include <chrono>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cout << "Uso correto: FastParseCLI <caminho_do_diretorio> <termo_de_busca>\n";
        std::cout << "Exemplo: FastParseCLI C:\\Projetos \"class\"\n";
        return 1;
    }

    std::filesystem::path targetDir(argv[1]);
    std::string_view searchToken(argv[2]);

    std::cout << "Iniciando varredura por: '" << searchToken << "' em " << targetDir << "...\n";

    auto startTime = std::chrono::high_resolution_clock::now();

    FileProcessor processor(searchToken);
    processor.scanDirectory(targetDir);

    auto endTime = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();

    processor.printResults();
    std::cout << "Tempo total de execucao: " << duration << " ms\n";

    return 0;
}