import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from website.models import Course, Chapter, Topic

def populate_database():
    print("Clearing existing Course, Chapter, and Topic data...")
    Topic.objects.all().delete()
    Chapter.objects.all().delete()
    Course.objects.all().delete()

    print("Creating 10 MBA Courses and detailed, deep tutorials...")

    courses_data = [
        {
            "title": "Strategic Management",
            "icon": "compass",
            "description": "Learn the frameworks used by executives to analyze markets, outline organizational direction, and sustain long-term competitive advantage.",
            "chapters": [
                {
                    "title": "Introduction to Business Strategy",
                    "order": 1,
                    "topics": [
                        {
                            "title": "What is Strategy?",
                            "order": 1,
                            "content": """
                            <p>In business, <strong>strategy</strong> is the coordinate set of commitments and actions designed to exploit core competencies and gain a competitive advantage. According to Michael Porter, strategy is about being different, choosing a unique set of activities to deliver a unique mix of value.</p>
                            
                            <h3>Operational Effectiveness vs. Strategy</h3>
                            <p>Many managers confuse operational effectiveness (OE) with strategy. OE means performing similar activities <em>better</em> than rivals. Strategy means performing <em>different</em> activities, or performing similar activities in <em>different ways</em>.</p>
                            
                            <table>
                                <thead>
                                    <tr>
                                        <th>Dimension</th>
                                        <th>Operational Effectiveness (OE)</th>
                                        <th>Strategic Positioning</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>Goal</strong></td>
                                        <td>Do things better, faster, cheaper</td>
                                        <td>Do things uniquely to capture premium value</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Focus</strong></td>
                                        <td>Best practices, efficiency, TQM, benchmarking</td>
                                        <td>Trade-offs, choosing what NOT to do</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Outcome</strong></td>
                                        <td>Competitive convergence (price wars)</td>
                                        <td>Sustainable competitive advantage</td>
                                    </tr>
                                </tbody>
                            </table>

                            <h3>Three Strategic Positions (Porter's Typology)</h3>
                            <p>Strategic positioning emerges from three distinct sources, which are not mutually exclusive and often overlap:</p>
                            <ul>
                                <li><strong>Variety-based positioning:</strong> Producing a subset of an industry’s products or services. It is based on the choice of product or service variety rather than customer segments. Example: <em>Jiffy Lube</em> specializes in automotive lubricants and does not offer other maintenance services.</li>
                                <li><strong>Needs-based positioning:</strong> Serving most or all of the needs of a particular group of customers. It comes close to traditional targeting of customer segments. Example: <em>IKEA</em> aims to meet all the home furnishing needs of its target buyers (price-sensitive consumers).</li>
                                <li><strong>Access-based positioning:</strong> Segmenting customers who are accessible in different ways. Although their needs are similar to those of other customers, the best configuration of activities to reach them is different. Example: <em>Carmike Cinemas</em> operates movie theaters exclusively in cities and towns with populations under 200,000.</li>
                            </ul>

                            <h3>The Role of Trade-offs</h3>
                            <p>A strategic position is not sustainable unless there are trade-offs with other positions. Trade-offs occur when activities are incompatible. Simply put, a trade-off means that more of one thing necessitates less of another. Trade-offs arise for three reasons: inconsistencies in image or reputation, limits on capacity/coordination, and differences in organizational values.</p>

                            <h3>Case Study: Southwest Airlines</h3>
                            <p>Southwest Airlines created a unique strategic position by serving price-sensitive travelers who would otherwise travel by car or bus. Southwest aligned all its activities to support this single strategy:</p>
                            <ul>
                                <li>No meals served on flights (reduces cost and turnaround time).</li>
                                <li>No seat assignments (encourages faster boarding).</li>
                                <li>Exclusive use of Boeing 737 aircraft (simplifies maintenance and training costs).</li>
                                <li>Point-to-point routes rather than hub-and-spoke systems (avoids congestion delays).</li>
                            </ul>
                            <p>Any competitor trying to copy Southwest would have to copy the entire system of activities, not just parts of it. Attempting to copy both Southwest and a traditional hub system (straddling) is what led to the failure of Continental Lite and Ted (United Airlines).</p>
                            """
                        },
                        {
                            "title": "Strategic Vision & Mission Statements",
                            "order": 2,
                            "content": """
                            <p>Strategic direction starts with clarifying where the company wants to go (Vision) and why the company exists (Mission).</p>
                            
                            <blockquote>
                                <strong>Vision Statement:</strong> A forward-looking, aspirational description of what an organization wants to achieve or become in the long-term (e.g., "To accelerate the world's transition to sustainable energy").
                            </blockquote>
                            
                            <blockquote>
                                <strong>Mission Statement:</strong> Focuses on the present business scope, clarifying the products, customer segments, and geographic markets served today.
                            </blockquote>
                            
                            <h3>Critical Success Factors for Vision Statements</h3>
                            <p>A vision statement is only useful if it motivates the workforce and guides decision-making. Excellent vision statements share several characteristics:</p>
                            <ul>
                                <li><strong>Inspirational:</strong> Excites employees and aligns stakeholders around a common purpose.</li>
                                <li><strong>Feasible:</strong> Challenging, but grounded in realistic market capacities and technological limits.</li>
                                <li><strong>Flexible:</strong> General enough to allow for pivoting in dynamic environments without needing a rewrite every year.</li>
                                <li><strong>Desirable:</strong> Appeals to the long-term interests of employees, customers, and shareholders.</li>
                            </ul>

                            <h3>The Value-focused Strategic Framework</h3>
                            <p>Corporate vision must flow down into values and actionable strategic goals. This hierarchy is often represented as follows:</p>
                            <ol>
                                <li><strong>Core Values:</strong> The beliefs and guiding principles that dictate behavior and decisions (e.g., integrity, sustainability).</li>
                                <li><strong>Mission:</strong> The definition of the current business model.</li>
                                <li><strong>Vision:</strong> The long-term aspirational target.</li>
                                <li><strong>Strategic Objectives:</strong> Specific, measurable milestones (SMART goals) to achieve the vision.</li>
                            </ol>

                            <h3>Case Study: Google's Mission Evolution</h3>
                            <p>Google’s original mission statement: <em>"To organize the world's information and make it universally accessible and useful."</em> This mission was incredibly clear and served as a filter for decisions. When considering new products (Search, Gmail, Maps), Google asked if it organized information. When Google restructured into Alphabet, it allowed the core company to stay focused on this mission while other entities (Waymo, Verily) pursued distinct strategic directions.</p>
                            """
                        }
                    ]
                },
                {
                    "title": "External Environment Analysis",
                    "order": 2,
                    "topics": [
                        {
                            "title": "Porter's Five Forces Framework",
                            "order": 1,
                            "content": """
                            <p>Developed by Michael E. Porter of Harvard Business School, the <strong>Five Forces Framework</strong> helps analyze the competitive forces in an industry environment that impact profitability.</p>
                            
                            <p>The strength of these five forces determines the industry's average profit potential:</p>
                            <ol>
                                <li><strong>Threat of New Entrants:</strong> Barriers to entry (economies of scale, capital requirements, switching costs, brand loyalty).</li>
                                <li><strong>Bargaining Power of Buyers:</strong> Buyers have power if they are concentrated, buy in large volumes, or can easily backward-integrate.</li>
                                <li><strong>Bargaining Power of Suppliers:</strong> Suppliers have power if they are dominated by a few firms, if switching costs are high, or if there are no substitutes.</li>
                                <li><strong>Threat of Substitute Products:</strong> Alternates outside the traditional industry border (e.g., train vs. airplane, or smartphones vs. standalone cameras).</li>
                                <li><strong>Rivalry Among Existing Competitors:</strong> Price cuts, advertising campaigns, and exit barriers.</li>
                            </ol>

                            <h3>How to Apply the Five Forces Analysis</h3>
                            <p>To analyze an industry, follow these steps:</p>
                            <ol>
                                <li><strong>Define the Industry:</strong> Identify the specific products/services and the geographic scope of the market.</li>
                                <li><strong>Identify the Actors:</strong> Group the competitors, buyers, suppliers, potential entrants, and substitutes.</li>
                                <li><strong>Determine the Strength of Each Force:</strong> Rate each force as Low, Medium, or High based on structural factors.</li>
                                <li><strong>Assess Overall Industry Attractiveness:</strong> Synthesize the findings. If forces are strong, profit margins are typically low. If forces are weak, profit potential is high.</li>
                            </ol>

                            <h3>Case Study: The Commercial Airline Industry</h3>
                            <p>The commercial airline industry is famous for having extremely low average profitability. Let's analyze why using the five forces:</p>
                            <ul>
                                <li><strong>Threat of Entrants (Medium-High):</strong> While capital requirements are high, leasing aircraft is relatively easy, and deregulation has lowered barriers.</li>
                                <li><strong>Power of Suppliers (High):</strong> Key suppliers (Boeing/Airbus for planes, jet fuel suppliers, pilots unions) have massive bargaining leverage.</li>
                                <li><strong>Power of Buyers (High):</strong> With search aggregators (Expedia, Google Flights), buyers have zero switching costs and buy on price.</li>
                                <li><strong>Threat of Substitutes (Medium):</strong> High-speed rail, video conferencing (reducing business travel), and driving.</li>
                                <li><strong>Rivalry (Very High):</strong> Fixed costs are high, marginal costs are low, and services are commoditized, leading to intense price competition.</li>
                            </ul>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Corporate Finance & Valuation",
            "icon": "landmark",
            "description": "Master financial modeling, capital structure analysis, investment appraisal metrics, and discount cash flow valuations.",
            "chapters": [
                {
                    "title": "Time Value of Money & Net Present Value",
                    "order": 1,
                    "topics": [
                        {
                            "title": "Time Value of Money (TVM)",
                            "order": 1,
                            "content": """
                            <p>The <strong>Time Value of Money (TVM)</strong> is the foundational concept that a dollar received today is worth more than a dollar received in the future due to its potential earning capacity (interest/investment returns).</p>
                            
                            <h3>Key Formulas</h3>
                            <p>The math behind TVM is based on compound interest, where interest earned is reinvested to earn more interest over time.</p>
                            <pre><code>Future Value (FV) = PV * (1 + r)^n
Present Value (PV) = FV / (1 + r)^n</code></pre>
                            <p>Where:</p>
                            <ul>
                                <li><em>PV</em> = Present Value</li>
                                <li><em>FV</em> = Future Value</li>
                                <li><em>r</em> = Discount/interest rate per period</li>
                                <li><em>n</em> = Number of periods</li>
                            </ul>

                            <h3>Numerical Example: Planning a Capital Expenditure</h3>
                            <p>Suppose your firm needs to purchase a $100,000 server rack in 3 years. If the company earns 8% annually on its cash reserves, how much must be set aside today to fund the purchase?</p>
                            <pre><code>PV = $100,000 / (1 + 0.08)^3
PV = $100,000 / 1.259712
PV = $79,383.22</code></pre>
                            <p>Thus, investing <strong>$79,383.22</strong> today at 8% interest will compound to exactly $100,000 in three years.</p>

                            <h3>Annuities and Perpetuities</h3>
                            <p>An <strong>annuity</strong> is a series of equal payments made at fixed intervals. A <strong>perpetuity</strong> is an annuity that continues indefinitely. The Present Value of a perpetuity is calculated as:</p>
                            <pre><code>PV of Perpetuity = C / r</code></pre>
                            <p>Where <em>C</em> is the cash flow per period and <em>r</em> is the discount rate. This formula is critical when calculating the Terminal Value in a Discounted Cash Flow (DCF) model.</p>
                            """
                        },
                        {
                            "title": "Net Present Value (NPV) & IRR Decision Rules",
                            "order": 2,
                            "content": """
                            <p>Corporate managers evaluate investments using Capital Budgeting metrics, primarily <strong>Net Present Value (NPV)</strong> and <strong>Internal Rate of Return (IRR)</strong>.</p>
                            
                            <h3>Net Present Value (NPV)</h3>
                            <p>NPV sums the present value of all cash inflows and outflows associated with a project. It represents the net dollar value added to the firm today.</p>
                            <pre><code>NPV = Σ [CF_t / (1 + r)^t] - Initial Investment</code></pre>

                            <h3>Internal Rate of Return (IRR)</h3>
                            <p>IRR is the specific discount rate that makes the NPV of all cash flows from a project equal to zero. It represents the expected annual yield of the investment.</p>

                            <h3>NPV vs. IRR comparison</h3>
                            <table>
                                <thead>
                                    <tr>
                                        <th>Metric</th>
                                        <th>Calculation Focus</th>
                                        <th>Decision Rule</th>
                                        <th>Primary Advantage</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>NPV</strong></td>
                                        <td>Absolute dollar value created</td>
                                        <td>Accept if NPV > 0</td>
                                        <td>Always theoretically correct; handles scale and changing interest rates.</td>
                                    </tr>
                                    <tr>
                                        <td><strong>IRR</strong></td>
                                        <td>Percentage rate of return</td>
                                        <td>Accept if IRR > Hurdle Rate</td>
                                        <td>Intuitively easier for executives to understand (e.g. 'this project yields 15%').</td>
                                    </tr>
                                </tbody>
                            </table>

                            <h3>Scenario: Mutually Exclusive Projects</h3>
                            <p>When selecting between two projects where you can only choose one, NPV should always be preferred over IRR. For example, Project A requires $10,000 and yields a 50% IRR ($15,000 return). Project B requires $10,000,000 and yields a 15% IRR ($11,500,000 return). IRR favors Project A, but Project B adds far more absolute wealth to the firm.</p>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Marketing Management",
            "icon": "megaphone",
            "description": "Understand consumer psychology, brand development strategies, target positioning, and modern marketing channel mixes.",
            "chapters": [
                {
                    "title": "Marketing Strategy Foundations",
                    "order": 1,
                    "topics": [
                        {
                            "title": "Segmentation, Targeting, and Positioning (STP)",
                            "order": 1,
                            "content": """
                            <p>The <strong>STP model</strong> is a structured approach to matching products with the right customer groups.</p>
                            
                            <h3>1. Market Segmentation</h3>
                            <p>Broad markets are rarely homogeneous. Marketers segment the population using four main variables:</p>
                            <ul>
                                <li><strong>Demographics:</strong> Age, gender, income, education, occupation (e.g., luxury watches targeted at high-income individuals).</li>
                                <li><strong>Geographics:</strong> Country, region, climate, urban vs. rural.</li>
                                <li><strong>Psychographics:</strong> Lifestyle, personality traits, values (e.g., active outdoors enthusiasts targeted by Patagonia).</li>
                                <li><strong>Behavioral:</strong> Brand loyalty, usage rate, benefit sought (e.g., business travelers seeking mileage rewards).</li>
                            </ul>

                            <h3>2. Targeting Strategies</h3>
                            <p>Once segments are defined, firms evaluate them based on segment size, growth potential, structural attractiveness, and company objectives. Firms then select their targeting strategy:</p>
                            <ul>
                                <li><strong>Undifferentiated (Mass) Marketing:</strong> Ignoring differences and targeting the entire market with one offer (e.g., standard Coca-Cola).</li>
                                <li><strong>Differentiated Marketing:</strong> Designing separate offers for several segments (e.g., Nike making running, basketball, and golf shoes).</li>
                                <li><strong>Niche (Concentrated) Marketing:</strong> Going after a large share of a small, specialized segment (e.g., Whole Foods targeting organic food buyers).</li>
                            </ul>

                            <h3>3. Positioning & The Positioning Statement</h3>
                            <p>Positioning is the act of designing the company's offering so that it occupies a distinctive place in the target customer's mind. It is summarized by a <strong>positioning statement</strong>:</p>
                            <blockquote>
                                "For <strong>[Target Customer]</strong>, our product is the <strong>[Category]</strong> that provides <strong>[Key Benefit]</strong>, unlike <strong>[Main Competitor]</strong> because <strong>[Differentiation Statement]</strong>."
                            </blockquote>
                            """
                        },
                        {
                            "title": "The 4 Ps of the Marketing Mix",
                            "order": 2,
                            "content": """
                            <p>The <strong>4 Ps</strong> (Product, Price, Place, Promotion) represents the tactical toolkit marketers use to execute their positioning strategy:</p>
                            
                            <h3>1. Product (Creating Value)</h3>
                            <p>The product is the total package of benefits the customer receives. It includes features, design, quality level, brand name, packaging, and ancillary services (like warranties or customer support).</p>
                            
                            <h3>2. Price (Capturing Value)</h3>
                            <p>Price is the only element in the marketing mix that produces revenue; all other elements represent costs. Common pricing strategies include:</p>
                            <ul>
                                <li><strong>Value-based Pricing:</strong> Setting prices based on the customer's perceived value rather than cost.</li>
                                <li><strong>Cost-plus Pricing:</strong> Adding a standard markup to the cost of the product.</li>
                                <li><strong>Penetration Pricing:</strong> Setting a low initial price to quickly capture market share.</li>
                                <li><strong>Price Skimming:</strong> Setting a high price initially to harvest demand from early adopters before lowering it.</li>
                            </ul>

                            <h3>3. Place (Delivering Value)</h3>
                            <p>Place refers to the channels and logistics used to make the product available to target customers. This includes distributors, wholesalers, retailers, and direct-to-consumer (DTC) digital commerce platforms.</p>

                            <h3>4. Promotion (Communicating Value)</h3>
                            <p>Promotion encompasses the activities used to inform, persuade, and remind customers about the product. The Integrated Marketing Communications (IMC) mix includes advertising, public relations, personal selling, sales promotion, and digital/social media marketing.</p>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Operations & Supply Chain Management",
            "icon": "truck",
            "description": "Explore bottlenecks, capacity calculations, inventory controls, Six Sigma quality architectures, and supply chain logistics.",
            "chapters": [
                {
                    "title": "Process Capacity & Bottlenecks",
                    "order": 1,
                    "topics": [
                        {
                            "title": "Little's Law and Bottleneck Identification",
                            "order": 1,
                            "content": """
                            <p>Operations management revolves around processing flows. A process is a network of activities that transforms inputs into higher-value outputs.</p>
                            
                            <h3>Little's Law</h3>
                            <p>Little's Law is a fundamental mathematical relation in queuing theory that applies to any stable system:</p>
                            <blockquote>
                                <strong>Little's Law Formula:</strong> Inventory (I) = Flow Rate (R) * Flow Time (T)
                            </blockquote>
                            <p>Where:</p>
                            <ul>
                                <li><strong>Inventory (I):</strong> The average number of units in the process (e.g. customers in a bank, or components in a factory).</li>
                                <li><strong>Flow Rate (R):</strong> The average rate at which units pass through the process (e.g. 50 parts/hour). Also referred to as throughput.</li>
                                <li><strong>Flow Time (T):</strong> The average time it takes a unit to go from start to finish through the process (e.g. 2 hours).</li>
                            </ul>

                            <h3>Identifying the Bottleneck</h3>
                            <p>The <strong>bottleneck</strong> is the resource/step in the system that has the lowest capacity (longest processing rate per unit). It determines the maximum output rate of the entire system. Adding capacity to non-bottleneck steps is waste; to increase system output, you must expand bottleneck capacity.</p>

                            <h3>Numerical Application: Airport Security</h3>
                            <p>Assume an airport security checkpoint has an average of 120 passengers waiting in line (Inventory). The security team processes an average of 6 passengers per minute (Flow Rate). What is the average wait time (Flow Time) for a passenger?</p>
                            <pre><code>Flow Time (T) = Inventory (I) / Flow Rate (R)
T = 120 passengers / 6 passengers per minute
T = 20 minutes</code></pre>
                            <p>A passenger spends an average of <strong>20 minutes</strong> in the security process.</p>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Organizational Behavior & HR",
            "icon": "users",
            "description": "Study human behavior in organizations. Explore motivational theories, leadership dynamics, team performance, and cultural alignment.",
            "chapters": [
                {
                    "title": "Motivational Theories in Action",
                    "order": 1,
                    "topics": [
                        {
                            "title": "Herzberg's Two-Factor Motivation Theory",
                            "order": 1,
                            "content": """
                            <p>Frederick Herzberg's <strong>Two-Factor Theory</strong> (Motivation-Hygiene Theory) suggests that job satisfaction and dissatisfaction act independently of each other.</p>
                            
                            <h3>Hygiene Factors vs. Motivators</h3>
                            <p>Herzberg argued that the factors that lead to satisfaction are completely separate from the factors that prevent dissatisfaction. He divided these into two categories:</p>
                            
                            <table>
                                <thead>
                                    <tr>
                                        <th>Hygiene Factors (Prevent Dissatisfaction)</th>
                                        <th>Motivators (Inspire Satisfaction & Output)</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Company policies and administration</td>
                                        <td>Sense of achievement</td>
                                    </tr>
                                    <tr>
                                        <td>Salary and benefits</td>
                                        <td>Recognition of work</td>
                                    </tr>
                                    <tr>
                                        <td>Physical working conditions</td>
                                        <td>Responsibility and autonomy</td>
                                    </tr>
                                    <tr>
                                        <td>Interpersonal relationships with peers/superiors</td>
                                        <td>Opportunity for advancement and personal growth</td>
                                    </tr>
                                </tbody>
                            </table>

                            <h3>Managerial Implications</h3>
                            <p>Managers must understand that simply increasing salaries or improving office layouts (Hygiene) will not motivate employees to work harder. It will only stop them from complaining. To increase productivity and engagement, managers must enrich jobs by giving employees more autonomy, responsibility, and opportunities for growth (Motivators).</p>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Managerial Economics",
            "icon": "trending-up",
            "description": "Apply microeconomic theories to firms. Master elasticity models, cost curves, market systems, and strategic game theories.",
            "chapters": [
                {
                    "title": "Market Structures & Game Theory",
                    "order": 1,
                    "topics": [
                        {
                            "title": "Oligopoly & Prisoners Dilemma",
                            "order": 1,
                            "content": """
                            <p>In oligopolies (markets with few dominant firms), pricing decisions are interdependent. We analyze these situations using <strong>Game Theory</strong>.</p>
                            
                            <h3>The Prisoner's Dilemma</h3>
                            <p>A classic game showing why two rational players might not cooperate, even if it is in their best interest to do so. In business, this explains pricing dilemmas between duopolists.</p>
                            
                            <table>
                                <thead>
                                    <tr>
                                        <th>Firm A / Firm B</th>
                                        <th>High Price (Cooperate)</th>
                                        <th>Low Price (Cheat)</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>High Price</strong></td>
                                        <td>$10M, $10M</td>
                                        <td>$2M, $15M</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Low Price</strong></td>
                                        <td>$15M, $2M</td>
                                        <td>$5M, $5M (Nash Equilibrium)</td>
                                    </tr>
                                </tbody>
                            </table>

                            <h3>Nash Equilibrium</h3>
                            <p>A Nash Equilibrium is a state in which no player has an incentive to unilaterally change their chosen strategy. In the matrix above, both firms choosing 'Low Price' is the Nash Equilibrium. Even though both would earn more ($10M each) by keeping prices high, fear of cheating drives both to price low and earn only $5M each.</p>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Business Analytics & Statistics",
            "icon": "bar-chart-3",
            "description": "Translate datasets into business decisions. Learn regression modeling, decision trees, forecasting, and data visualization.",
            "chapters": [
                {
                    "title": "Predictive Modeling Basics",
                    "order": 1,
                    "topics": [
                        {
                            "title": "Simple Linear Regression for Forecasting",
                            "order": 1,
                            "content": """
                            <p><strong>Linear Regression</strong> is a statistical method used to model the relationship between a dependent variable (Y) and an independent variable (X).</p>
                            
                            <h3>Regression Formula</h3>
                            <pre><code>Y = β0 + β1*X + ε</code></pre>
                            <p>Where:</p>
                            <ul>
                                <li><strong>Y:</strong> The dependent variable you want to predict (e.g. Sales).</li>
                                <li><strong>X:</strong> The independent variable (e.g. Marketing Spend).</li>
                                <li><strong>β0:</strong> The Y-intercept (value of Y when X is 0).</li>
                                <li><strong>β1:</strong> The slope (how much Y increases for every unit increase in X).</li>
                                <li><strong>ε:</strong> The residual error term.</li>
                            </ul>

                            <h3>Evaluating the Model: R-Squared</h3>
                            <p>The <strong>Coefficient of Determination (R-squared)</strong> measures how much of the variation in the dependent variable is explained by the independent variable. It ranges from 0 to 1 (or 0% to 100%). A higher R-squared indicates a better fit of the regression line to the data.</p>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Entrepreneurship & Venture Capital",
            "icon": "rocket",
            "description": "Learn the process of building high-growth startups, drafting business models, raising venture financing, and calculating cap tables.",
            "chapters": [
                {
                    "title": "The Lean Startup Framework",
                    "order": 1,
                    "topics": [
                        {
                            "title": "The Build-Measure-Learn Loop",
                            "order": 1,
                            "content": """
                            <p>Popularized by Eric Ries, the <strong>Lean Startup Methodology</strong> advocates for developing products iteratively to reduce market risk.</p>
                            
                            <h3>The Feedback Loop</h3>
                            <p>Startups fail when they build products that nobody wants. The Lean Startup prevents this by encouraging rapid iteration through the <strong>Build-Measure-Learn</strong> feedback loop:</p>
                            <ul>
                                <li><strong>Build:</strong> Put together a Minimum Viable Product (MVP) with the smallest feature set needed to test hypotheses about customer needs.</li>
                                <li><strong>Measure:</strong> Collect quantitative usage data and qualitative user feedback from early adopters.</li>
                                <li><strong>Learn:</strong> Analyze data to decide whether to <strong>Pivot</strong> (change core assumptions, target segments, or product direction) or <strong>Persevere</strong> (keep building and scaling the existing plan).</li>
                            </ul>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Negotiation & Conflict Resolution",
            "icon": "handshake",
            "description": "Develop strategic bargaining skills. Master ZOPA boundaries, BATNA fallback strategies, and integrative win-win agreements.",
            "chapters": [
                {
                    "title": "Negotiation Core Concepts",
                    "order": 1,
                    "topics": [
                        {
                            "title": "BATNA & ZOPA Boundaries",
                            "order": 1,
                            "content": """
                            <p>Strategic negotiation depends on preparation and quantifying boundaries.</p>
                            
                            <h3>BATNA (Best Alternative to a Negotiated Agreement)</h3>
                            <p>Your BATNA is your fallback option if the current negotiation collapses. It represents your power in the negotiation. If you have a strong BATNA (e.g. another job offer), you can walk away from poor deals.</p>
                            
                            <h3>ZOPA (Zone of Possible Agreement)</h3>
                            <p>The ZOPA is the overlapping price range between the buyer's maximum willingness to pay (Reservation Price) and the seller's minimum willingness to accept.</p>
                            
                            <p>If the buyer's reserve price is $100 and the seller's reserve price is $80, a ZOPA exists between $80 and $100. If the seller demands at least $110, no agreement is possible.</p>
                            """
                        }
                    ]
                }
            ]
        },
        {
            "title": "Corporate Governance & Ethics",
            "icon": "scale",
            "description": "Analyze corporate structures, duties of directors, investor protections, CSR models, and business ethical frameworks.",
            "chapters": [
                {
                    "title": "Corporate Responsibility & Governance Systems",
                    "order": 1,
                    "topics": [
                        {
                            "title": "Agency Theory and Principal-Agent Conflict",
                            "order": 1,
                            "content": """
                            <p><strong>Agency Theory</strong> addresses conflicts of interest between shareholders (Principals) and managers (Agents).</p>
                            
                            <h3>The Conflict</h3>
                            <p>Principals want to maximize shareholder wealth. Agents (managers) may want to maximize their own salary, job security, or power, leading to agency costs. Governance systems align these interests:</p>
                            <ul>
                                <li><strong>Stock Options:</strong> Linking executive compensation to stock price.</li>
                                <li><strong>Board of Directors:</strong> Representing shareholders to monitor and hire/fire managers.</li>
                                <li><strong>Audits:</strong> Ensuring financial numbers are not manipulated.</li>
                            </ul>
                            """
                        }
                    ]
                }
            ]
        }
    ]

    for c_data in courses_data:
        course = Course.objects.create(
            title=c_data["title"],
            icon=c_data["icon"],
            description=c_data["description"]
        )
        print(f"Created Course: {course.title}")

        for ch_data in c_data["chapters"]:
            chapter = Chapter.objects.create(
                course=course,
                title=ch_data["title"],
                order=ch_data["order"]
            )
            print(f"  Created Chapter: {chapter.title}")

            for t_data in ch_data["topics"]:
                topic = Topic.objects.create(
                    chapter=chapter,
                    title=t_data["title"],
                    order=t_data["order"],
                    content=t_data["content"],
                    is_published=True
                )
                print(f"    Created Topic: {topic.title}")

    print("\nDatabase seeding completed successfully!")

if __name__ == "__main__":
    populate_database()
