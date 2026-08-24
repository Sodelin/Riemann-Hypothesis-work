import Zeta23.Statement
import Zeta23.ExplicitFormula

namespace RHResearch

-- These checks deliberately use the upstream names directly. Their purpose is to make
-- dependency drift fail loudly in CI rather than silently changing the research seam.

#check RiemannHypothesis
#check Zeta23.IsNontrivialZero
#check Zeta23.zeroMult
#check Zeta23.EF.weilTest
#check Zeta23.EF.paperFT_weilTest
#check Zeta23.EF.EF_lit
#check Zeta23.EF.EF_paper

end RHResearch
