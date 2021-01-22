import org.apache.commons.math3.stat.inference.TTest;
import java.util.Arrays;

public class HypoAnalysis {
    public static void main(String[] args) {
        if (args.length != 5) {
            System.out.println("Error: ReconfTtest reconfSampleNum reconfSampleFailureNum nonReconfSampleNum nonReconfSampleFailureNum confidence");
            System.exit(-1);
        }
        final int reconfSampleNum = Integer.valueOf(args[0]);
        final int reconfSampleFailureNum = Integer.valueOf(args[1]);
        final int nonReconfSampleNum = Integer.valueOf(args[2]);
        final int nonReconfSampleFailureNum = Integer.valueOf(args[3]);
	double alpha = 1.0 - Double.valueOf(args[4]); // 1.0 - 0.8 = 0.2
	final double succeedValue = 0;
        final double failValue = 1;

        double[] reconfSamples = new double[reconfSampleNum];
        Arrays.fill(reconfSamples, succeedValue);
        for (int i=0; i<reconfSampleFailureNum; i++) {
            reconfSamples[i] = failValue;
        }
        double[] nonReconfSamples = new double[nonReconfSampleNum];
        Arrays.fill(nonReconfSamples, succeedValue);
        for (int i=0; i<nonReconfSampleFailureNum; i++) {
            nonReconfSamples[i] = failValue;
        }
        
        TTest tt = new TTest();
        boolean null_hypothesis = !tt.pairedTTest(reconfSamples, nonReconfSamples, alpha);
        System.out.println("null_hypothesis is " + null_hypothesis);
    }
}
