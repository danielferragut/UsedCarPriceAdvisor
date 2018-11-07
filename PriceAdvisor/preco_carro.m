function preco_carro
    arquivo_csv = argv(){1};
    ano = input("Digite o ano do seu carro: ");
    quilometragem = input("Digite a quilometragem do seu carro: ");
    dados = csvread(arquivo_csv);

    dados_normalizados = normalize(dados);
    matrix_phi = generate_phi(dados_normalizados);
    coeficientes = solve_for_phi(matrix_phi, dados_normalizados(:,1));
    input_normalizado = normalize_melissa(dados, [ano,quilometragem]);

    preco_sugerido_normalizado = solve_for_ano_quilo(coeficientes, input_normalizado(1), input_normalizado(2));
    preco_sugerido = denormalize_melissa(dados, preco_sugerido_normalizado);
    

    printf("Sugestao de preco: R$");
    printf(num2str(preco_sugerido));
    printf(".\n");
endfunction


function retorno = normalize (data)

    mean_price = mean(data(:,1));
    mean_year = mean(data(:,2));
    mean_kilom = mean(data(:,3));

    max_price = max(data(:,1));
    max_year = max(data(:,2));
    max_kilom = max(data(:,3));

    min_price = min(data(:,1));
    min_year = min(data(:,2));
    min_kilom = min(data(:,3));

    data(:,1) = (data(:,1) - mean_price)/(max_price - min_price);
    data(:,2) = (data(:,2) - mean_year)/(max_year - min_year);
    data(:,3) = (data(:,3) - mean_kilom)/(max_kilom - min_kilom);

    retorno = data;

endfunction


function norm = normalize_melissa(data, melissa)

    norm = ones(1, 2);

    mean_year = mean(data(:,2));
    mean_kilom = mean(data(:,3));

    max_year = max(data(:,2));
    max_kilom = max(data(:,3));

    min_year = min(data(:,2));
    min_kilom = min(data(:,3));

    norm(1) = (melissa(1) - mean_year)/(max_year - min_year);
    norm(2) = (melissa(2) - mean_kilom)/(max_kilom - min_kilom);

endfunction

function price = denormalize_melissa(data, result_melissa)  

    mean_price = mean(data(:,1));
    max_price = max(data(:,1));
    min_price = min(data(:,1));

    price = result_melissa*(max_price - min_price) + mean_price;
endfunction

function phi = generate_phi (x)
    m = size(x)(1);
    phi = zeros(m, 6);
    phi(:,1) = ones(m, 1);
    phi(:,2) =  x(:,2);
    phi(:,3) =  x(:,3);
    phi(:,4) =  x(:,2) .* x(:,2);
    phi(:,5) =  x(:,2) .* x(:,3);
    phi(:,6) =  x(:,3) .* x(:,3);
endfunction

function coefficients = solve_for_phi(phi, y)
    A = phi'*phi;
    B = phi'*y;
    coefficients = A\B; 
endfunction

function preco=solve_for_ano_quilo(coeficientes, ano, quilometragem)
    preco = 0;
    termo1 = coeficientes(1)
    termo2 = coeficientes(2)*ano
    termo3 = coeficientes(3)*quilometragem
    termo4 = coeficientes(4)*ano*ano
    termo5 = coeficientes(5)*quilometragem*ano
    termo6 = coeficientes(6)*quilometragem*quilometragem
    preco = termo1+termo2+termo3+termo4+termo5+termo6;
endfunction
