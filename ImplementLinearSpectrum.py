masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
          'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def linearSpectrum(peptide):
    prefixMass = [0]
    for i in range(0, len(peptide) - 1):
        prefixMass.append(prefixMass[i] + masses[peptide[i]])
    prefixMass.append(prefixMass[-1] + masses[peptide[-1]])
    spectrum = [0]
    for i in range(len(peptide) + 1):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefixMass[j] - prefixMass[i])
    return sorted(spectrum)


peptide = ''
print (*linearSpectrum(peptide), sep = ' ')
