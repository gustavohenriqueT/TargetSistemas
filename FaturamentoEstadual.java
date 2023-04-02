package target.sistemas;

import java.text.NumberFormat;
import java.util.HashMap;
import java.util.Map;

public class FaturamentoEstadual {

	public static void main(String[] args) {

		// Faturamento mensal por estado
		Map<String, Double> faturamento = new HashMap<>();
		faturamento.put("SP", 67836.43);
		faturamento.put("RJ", 36678.66);
		faturamento.put("MG", 29229.88);
		faturamento.put("ES", 27165.48);
		faturamento.put("Outros", 19849.53);

		// Cálculo do faturamento total
		double faturamentoTotal = faturamento.values().stream().mapToDouble(Double::doubleValue).sum();

		// Cálculo do percentual de representação de cada estado
		Map<String, Double> percentuais = new HashMap<>();
		for (Map.Entry<String, Double> entry : faturamento.entrySet()) {
			double percentual = entry.getValue() / faturamentoTotal * 100;
			percentuais.put(entry.getKey(), percentual);
		}

		// Impressão dos resultados
		NumberFormat nf = NumberFormat.getInstance();
		nf.setMaximumFractionDigits(2);
		System.out.println("Percentual de representação por estado:");
		for (Map.Entry<String, Double> entry : percentuais.entrySet()) {
			System.out.println(entry.getKey() + " - R$" + nf.format(entry.getValue()) + "%");
		}
	}

}