import { UserRepository } from '../../repositories/users/UserRepository';
import { User } from '../../models/User';
import { validateEmail, validatePassword } from '../../validators/userValidators';

export class UserService {
    private userRepository: UserRepository;

    constructor() {
        this.userRepository = new UserRepository();
    }

    public async register(email: string, password: string): Promise<User> {
        validateEmail(email);
        validatePassword(password);
        const user = await this.userRepository.create({ email, password });
        // Here you would send a confirmation email
        return user;
    }
}
